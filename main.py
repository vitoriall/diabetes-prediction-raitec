from src.data_processing import load_data, clean_data
from src.model_training import split_data, train_model
from src.evaluation import evaluate_model
import joblib
import os

def run_model(model_name):
    print(f"\n===== Avaliando Modelo: {model_name.replace('_', ' ').title()} =====")
    df = load_data('data/diabetes.csv')
    df = clean_data(df)
    X_train, X_test, y_train, y_test = split_data(df)
    model = train_model(X_train, y_train, model_name)
    evaluate_model(model, X_test, y_test)

    if model_name == 'random_forest':
        # Criar a pasta se não existir
        os.makedirs('modelos', exist_ok=True)
        joblib.dump(model, 'modelos/random_forest_model.joblib')
        print("✅ Modelo Random Forest salvo em: modelos/random_forest_model.joblib")


def main():
    for model_name in ['decision_tree', 'random_forest', 'logistic_regression']:
        run_model(model_name)

if __name__ == '__main__':
    main()