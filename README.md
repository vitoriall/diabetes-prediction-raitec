# 🧠 Projeto RAITec Apoio 2025.1 – Modelo Preditivo de Diabetes

Este repositório contém todas as etapas do desenvolvimento de um modelo de Machine Learning supervisionado para prever o risco de diabetes a partir de dados clínicos simples. O projeto foi realizado por membros do eixo de Apoio do RAITec durante o ciclo trainee 2025.1.

---

## 📌 Objetivo

Construir um pipeline completo e funcional de machine learning, desde a limpeza dos dados até a geração de previsões, usando um dataset real. O modelo final foi escolhido com base em métricas como recall, f1-score e acurácia.

---

## 🧪 Dataset Utilizado

- **Nome:** Pima Indians Diabetes Database  
- **Fonte:** [Kaggle](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

---

## 🗂️ Estrutura do Projeto

diabetes-prediction-raitec/
├── data/               # Dataset original (.csv)
├── notebooks/          # Scripts de análise exploratória
├── src/                # Scripts principais (processamento, treino, avaliação)
├── models/             # Modelos salvos (.joblib)
├── graficos/           # Outputs gerados (gráficos, matrizes)
├── main.py             # Pipeline completo de execução
├── predict.py          # Script interativo de predição
├── requirements.txt    # Dependências do projeto
└── README.md           # Este documento

---

## ⚙️ Tecnologias e Ferramentas

- Python 3.10+

- VS Code

- Git + GitHub

- Overleaf (documentação)

- Trello (SCRUM)

- Bibliotecas: pandas, numpy, seaborn, matplotlib, scikit-learn, joblib

---

## 👩‍💻 Etapas do Projeto
1. 📥 Pré-processamento (data_processing.py)
Identificação de valores 0 inválidos (ex: glicose = 0)

- Substituição por NaN e preenchimento com média da coluna

- Estatísticas descritivas

## 2. 📊 Análise Exploratória (eda_automatica.py)
Geração de histogramas, boxplots, heatmap, pairplot

- Visualização da distribuição por classe

- Gráficos salvos na pasta /graficos

## 3. 🤖 Modelagem (model_training.py)
Modelos testados:

- Decision Tree

- Random Forest ✅ (escolhido)

- Logistic Regression

- Divisão em treino e teste (80/20)

## 4. 📈 Avaliação (evaluation.py)
Geração da matriz de confusão

Métricas:

- Acurácia: 75%

- Recall (classe 1): 0.65

- F1-score: 0.65

- Salvamento do modelo Random Forest com joblib

## 5. 🧪 Predição (predict.py)
- Recebe dados via terminal

- Carrega o modelo salvo

- Retorna o resultado: 0 (sem risco) ou 1 (com risco)

## 👥 Divisão de Responsabilidades
| Membro   | Responsável por             |
| -------- | --------------------------- |
| Vitória  | Dados e Pré-processamento   |
| Kim      | Análise Exploratória (EDA)  |
| Amanda   | Modelagem                   |
| Bruno    | Avaliação e Salvamento      |
| Pessoa 5 | Integração Final e Predição |

## 📄 Documentação
- A documentação final foi elaborada em LaTeX no Overleaf, seguindo o modelo oficial do RAITec. Inclui:

- Visão geral do projeto

- Etapas de desenvolvimento

- Resultados

- Sugestões de aprimoramento

- Conclusão e contribuições para o eixo de Apoio

## 📚 Referências
- Pima Indians Diabetes Dataset – Kaggle

- Scikit-learn Documentation

- Cursos de Python e ML –  YouTube