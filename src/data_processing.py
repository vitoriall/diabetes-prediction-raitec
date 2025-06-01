import pandas as pd
import numpy as np

def load_data(filepath):
    """Carrega o dataset a partir do caminho informado."""
    return pd.read_csv(filepath)

def clean_data(df):
    """Substitui valores zero por NaN nas colunas onde zero não faz sentido
    e preenche os valores ausentes com a média da coluna."""
    cols_with_zero = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    df[cols_with_zero] = df[cols_with_zero].replace(0, np.nan)
    df.fillna(df.mean(), inplace=True)
    return df

if __name__ == '__main__':
    # Executa carregamento e limpeza
    df = load_data('data/diabetes.csv')
    df = clean_data(df)

    # Exibe estatísticas do dataframe limpo
    print("Resumo estatístico dos dados tratados:")
    print(df.describe())