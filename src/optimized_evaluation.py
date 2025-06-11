import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    recall_score, precision_score, classification_report,
    confusion_matrix
)

def load_data(filepath):
    "Carrega o dataset a partir do caminho informado."
    return pd.read_csv(filepath)

def clean_data(df):
    """Substitui valores zero por NaN nas colunas onde zero não faz sentido
    e preenche os valores ausentes com a mediana da coluna."""
    cols_with_zero = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    df[cols_with_zero] = df[cols_with_zero].replace(0, np.nan)
    df.fillna(df.median(), inplace=True)
    return df

def train_model(X_train, y_train):
    "Treina o modelo Random Forest com peso maior para classe positiva."
    model = RandomForestClassifier(class_weight={0: 1, 1: 3}, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test, limiar=0.3):
    "Avalia o modelo com limiar ajustado e imprime métricas."
    y_proba = model.predict_proba(X_test)[:, 1]
    y_pred = (y_proba >= limiar).astype(int)

    recall = recall_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    print(f"Recall da classe 1 (positiva): {recall:.4f}")
    print(f"Precision da classe 1 (positiva): {precision:.4f}\n")
    print("Relatório completo:\n")
    print(classification_report(y_test, y_pred, digits=4))
    
    # Matriz de confusão
    print(f"Matriz de Confusão:\n {cm}")

    return y_pred

if __name__ == '__main__':
    # Caminho do dataset
    filepath = 'data/diabetes.csv'

    # 1. Carregar e limpar os dados
    df = load_data(filepath)
    df = clean_data(df)

    # 2. Separar variáveis
    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]

    # 3. Dividir em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 4. Treinar o modelo
    model = train_model(X_train, y_train)

    # 5. Avaliar o modelo com limiar ajustado
    y_pred = evaluate_model(model, X_test, y_test, limiar=0.3)

