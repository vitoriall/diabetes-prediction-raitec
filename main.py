import os
from notebooks.eda_automatica import load_and_clean_data, gerarHistogramas, gerarBoxplots, gerarHeatmap, gerarPairplot
from src.model_training import train_and_evaluate
import joblib

def run_eda():
    print("Iniciando análise exploratória dos dados...")
    caminho_csv = 'data/diabetes.csv'
    df = load_and_clean_data(caminho_csv)
    gerarHistogramas(df)
    gerarBoxplots(df)
    gerarHeatmap(df)
    gerarPairplot(df)
    print("Análise exploratória concluída! Gráficos salvos em ./graficos/")

def main():
    # 1. Rodar EDA (análise exploratória de dados)
    run_eda()

    # 2. Treinar e avaliar modelos
    print("\nIniciando pipeline completo de treinamento e avaliação...")

    models_to_test = ['decision_tree', 'random_forest', 'logistic_regression']
    best_model_name = None
    best_accuracy = 0
    best_model = None

    for model_name in models_to_test:
        model, y_pred, y_test = train_and_evaluate(model_name)

        # Vamos usar acurácia simples para escolher melhor modelo
        from sklearn.metrics import accuracy_score
        acc = accuracy_score(y_test, y_pred)
        if acc > best_accuracy:
            best_accuracy = acc
            best_model_name = model_name
            best_model = model

    # 3. Salvar o melhor modelo
    os.makedirs('models', exist_ok=True)
    model_path = os.path.join('models', 'final_model.pkl')
    joblib.dump(best_model, model_path)
    print(f"\nModelo salvo em {model_path}")
    print(f"Melhor modelo: {best_model_name.replace('_', ' ').title()} com acurácia {best_accuracy:.4f}")

if __name__ == "__main__":
    main()
