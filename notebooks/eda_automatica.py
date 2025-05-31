# -*- coding: utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_csv('data/diabetes.csv')

# Substituir zeros por NaN e preencher com média
cols_with_zero = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df[cols_with_zero] = df[cols_with_zero].replace(0, pd.NA)
df = df.fillna(df.mean())

# Estatísticas descritivas
print("Estatísticas descritivas:")
print(df.describe())
print("\nDistribuição de classes (Outcome):")
print(df['Outcome'].value_counts())

# Heatmap de correlação
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Mapa de Correlação')
plt.tight_layout()
plt.savefig('outputs/heatmap_correlacao.png')
plt.close()

# Histogramas por variável
for col in df.columns[:-1]:
    plt.figure()
    sns.histplot(data=df, x=col, hue='Outcome', kde=True, element="step")
    plt.title(f'Distribuição de {col} por classe')
    plt.tight_layout()
    plt.savefig(f'outputs/hist_{col}.png')
    plt.close()

# Boxplots por variável
for col in df.columns[:-1]:
    plt.figure()
    sns.boxplot(data=df, x='Outcome', y=col)
    plt.title(f'Boxplot de {col} por classe')
    plt.tight_layout()
    plt.savefig(f'outputs/boxplot_{col}.png')
    plt.close()

# Pairplot completo
sns.pairplot(df, hue='Outcome')
plt.suptitle('Pairplot das variáveis por classe', y=1.02)
plt.savefig('outputs/pairplot.png')
plt.close()
