import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os 

# Configura o visual dos gráficos
sns.set(style = 'whitegrid')

# Cria uma pasta chamada "graficos"
os.makedirs("graficos", exist_ok = True)

# Carrega e trata os dados
def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    cols_with_zero = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    df[cols_with_zero] = df[cols_with_zero].replace(0, pd.NA)
    df = df.fillna(df.mean())
    return df

# Gera histogramas
def gerarHistogramas(df):
    for col in df.columns[:-1]: 
        plt.figure(figsize = (8, 4))
        sns.histplot(data = df, x = col, hue = 'Outcome', kde = True, element = 'step')
        plt.title(f'Histograma de {col}')
        plt.tight_layout()
        plt.savefig(f'graficos/hist_{col}.png')
        plt.close()

# Gera boxplots
def gerarBoxplots(df):
    for col in df.columns[:-1]:
        plt.figure(figsize = (8, 4))
        sns.boxplot(x = 'Outcome', y = col, data = df)
        plt.title(f'Boxplot de {col} por classe')
        plt.tight_layout()
        plt.savefig(f'graficos/box_{col}.png')
        plt.close()

# Mapa de correlação
def gerarHeatmap(df):
        plt.figure(figsize = (10, 8))
        sns.heatmap(df.corr(), annot = True, cmap = 'coolwarm', fmt = ".2f")
        plt.title('Mapa de Correlação')
        plt.tight_layout()
        plt.savefig('graficos/heatmap_correlacao.png')
        plt.close()

# Pairplot
def gerarPairplot(df):
    pair = sns.pairplot(df, hue = 'Outcome', corner = True)
    pair.fig.suptitle('Pairplot das variáveis', y = 1.02)
    pair.savefig('graficos/pairplot.png')
    plt.close()

# Carrega, limpa e gera os gráficos
if __name__ == '__main__':
    caminho_csv = 'data/diabetes.csv'
    df = load_and_clean_data(caminho_csv)

    gerarHistogramas(df)
    gerarBoxplots(df)
    gerarHeatmap(df)
    gerarPairplot(df)
print ("tomate")
