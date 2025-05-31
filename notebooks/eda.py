import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv('data/diabetes.csv')

# Tratar dados faltantes
cols_with_zero = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df[cols_with_zero] = df[cols_with_zero].replace(0, pd.NA)
df = df.fillna(df.mean())

# Estatísticas básicas
print(df.describe())
print(df['Outcome'].value_counts())

# Mapa de correlação
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Mapa de Correlação')
plt.tight_layout()
plt.show()

# Distribuição por classe
for col in df.columns[:-1]:
    sns.histplot(data=df, x=col, hue='Outcome', kde=True, element="step")
    plt.title(f'Distribuição de {col} por classe')
    plt.tight_layout()
    plt.show()
