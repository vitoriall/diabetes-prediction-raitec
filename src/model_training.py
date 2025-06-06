# Importando funções de carregamento e limpeza dos dados
from src.data_processing import load_data, clean_data

# Importando bibliotecas para divisão dos dados, modelos e métricas de avaliação
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, classification_report

# Função para dividir o dataframe em treino e teste
def split_data(df, target_col='Outcome', test_size=0.2, random_state=42):
    X = df.drop(columns=[target_col])  # Features
    y = df[target_col]  # Rótulo (alvo)
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

# Função para instanciar o modelo de acordo com o nome informado
def get_model(model_name):
    if model_name == 'decision_tree':
        return DecisionTreeClassifier(random_state=42)
    elif model_name == 'random_forest':
        return RandomForestClassifier(n_estimators=100, random_state=42)
    elif model_name == 'logistic_regression':
        return LogisticRegression(max_iter=1000, random_state=42)
    else:
        raise ValueError(f"Modelo '{model_name}' não implementado.")

# Função principal que treina e avalia o modelo
def train_and_evaluate(model_name, filepath='data/diabetes.csv'):
    raw_df = load_data(filepath)            # Carregamento do CSV bruto
    cleaned_df = clean_data(raw_df)         # Limpeza/preparação dos dados

    X_train, X_test, y_train, y_test = split_data(cleaned_df)  # Separação dos dados

    model = get_model(model_name)           # Seleciona e instancia o modelo
    model.fit(X_train, y_train)             # Treina o modelo

    y_pred = model.predict(X_test)          # Faz previsões no conjunto de teste

    # Breve avaliação do modelo
    print(f"\n--- Resultados para o Modelo: {model_name.replace('_', ' ').title()} ---")
    print("Acurácia:", accuracy_score(y_test, y_pred))
    print("Recall:", recall_score(y_test, y_pred))
    print("Relatório de Classificação:\n", classification_report(y_test, y_pred))

    return model, y_pred, y_test

# Executa o código abaixo apenas se o script for rodado diretamente
if __name__ == "__main__":
    print("Iniciando treinamento e avaliação dos modelos...")

    # Lista com os modelos que vamos testar
    models_to_test = ['decision_tree', 'random_forest', 'logistic_regression']

    trained_models = {}  # Dicionário para guardar os modelos e seus resultados

    for model_name in models_to_test:
        model, y_pred, y_test_actual = train_and_evaluate(model_name)
        trained_models[model_name] = {
            'model': model,
            'y_pred': y_pred,
            'y_test': y_test_actual
        }
