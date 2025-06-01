# 🧠 Projeto RAITec 2025.1 – Etapa 1: Dados e Pré-processamento

Este repositório representa a **primeira etapa do projeto de Machine Learning** proposto na trilha de Apoio do Trainee RAITec 2025.1.  
O objetivo é preparar os dados para a construção de um modelo preditivo de risco de diabetes.

---

## ✅ O que já foi feito

### 📁 Estrutura atual do projeto:

diabetes-prediction/
├── data/                  # Dataset original (não versionado)
│   └── diabetes.csv       # Arquivo de dados
├── src/                   # Scripts em Python
│   └── data_processing.py # Carregamento e limpeza dos dados
├── .gitignore             # Arquivos/pastas ignoradas no Git
└── README.md              # Este arquivo


### 📌 Explicação do que foi implementado:

#### `src/data_processing.py`
- Lê o arquivo `diabetes.csv`
- Substitui valores zero por `NaN` nas colunas em que **zero não é um valor possível** (como glicose ou pressão arterial)
- Preenche os dados ausentes com a **média da coluna**
- Exibe o resumo estatístico final com `describe()`

#### `.gitignore`
- Evita versionar pastas e arquivos que não precisam ir para o GitHub, como:
  - `__pycache__`, arquivos `.pyc`
  - Saídas (`/outputs`) ou modelos salvos (`/modelos`)
  - Checkpoints do Jupyter

---

## 🧪 Por que essa etapa é importante?

- O modelo de Machine Learning depende de **dados limpos e consistentes** para aprender.
- Zeros em variáveis como glicose, BMI ou insulina podem gerar **ruído ou distorcer os resultados**.
- Essa etapa garante que os dados estejam **preparados corretamente** antes de gerar qualquer gráfico ou treinar um modelo.

---

## 🔜 Próximos passos (para os membros do grupo)

### 👤 Amanda – Análise Exploratória (EDA)
- Criar o script `notebooks/eda_automatica.py`
- Gerar gráficos:
  - Heatmap de correlação
  - Histogramas e boxplots por classe
  - Pairplot (opcional)
- Salvar todos os gráficos em `/outputs`

### 👤 Camille – Modelagem
- Criar `src/model_training.py`
- Testar modelos: Decision Tree, Random Forest, Logistic Regression
- Separar treino/teste e treinar os modelos

### 👤 Bruno – Avaliação
- Criar `src/evaluation.py`
- Gerar métricas: acurácia, recall, f1-score, matriz de confusão
- Escolher o melhor modelo
- Salvar modelo com `joblib` em `/modelos`

### 👤 Pessoa 5 – Integração e Predição
- Criar `main.py` para rodar todo o projeto
- Criar `predict.py` para simular entrada de dados reais no modelo salvo

---

## 📌 Dataset utilizado

- Nome: **Pima Indians Diabetes Database**
- Fonte: Kaggle  
🔗 [Acesse o dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

---


