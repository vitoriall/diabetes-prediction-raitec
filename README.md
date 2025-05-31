# 🧠 Modelo Preditivo de Diabetes – RAITec Apoio 2025.1

Este projeto tem como objetivo desenvolver um modelo de machine learning capaz de prever o risco de diabetes com base em dados médicos simples. Ele faz parte do eixo de Apoio da etapa trainee do RAITec.

---

## 📁 Estrutura do Projeto

📦 diabetes-prediction/
├── data/ # Dataset original (não versionado)
├── modelos/ # Modelos treinados (.joblib)
├── notebooks/ # Análises exploratórias
├── outputs/ # Gráficos e matrizes geradas
├── src/ # Scripts principais do pipeline
├── main.py # Executa os modelos
├── requirements.txt # Bibliotecas
├── README.md # Este arquivo


---

## ✅ Status Atual

### ✔️ Etapas já concluídas:
- [x] Análise Exploratória completa (gráficos, correlações, insights)
- [x] Modelagem com 3 algoritmos:
  - Decision Tree
  - Random Forest
  - Logistic Regression
- [x] Avaliação comparativa das métricas
- [x] Salvamento do melhor modelo (`random_forest_model.joblib`)
- [x] Organização do projeto no Trello com metodologia SCRUM

### 🚧 A fazer:
- Criar interface de predição (`predict.py`)
- Implementar desafio adicional com dados temporais
- Finalizar documentação no Overleaf
- Preparar slides da apresentação

---

## 🚀 Como Executar

### 1. Instale as dependências:
```bash```

pip install -r requirements.txt

2. Execute o modelo:

python main.py

Isso irá:

Carregar e limpar os dados

Treinar os modelos

Avaliar e imprimir as métricas

Salvar o modelo Random Forest em /modelos/

## 📈 Resultados e Insights

- **Glucose** foi a variável mais correlacionada com risco de diabetes (correlação ≈ 0.49)
- **BMI** e **Age** também apresentaram forte influência
- O **Random Forest** foi o melhor modelo:
  - Recall classe 1: 0.65
  - Acurácia: 75%
  - F1-score: 0.65
- Boxplots, histogramas e heatmaps estão salvos na pasta `/outputs`

## 🤝 Como contribuir com o projeto

1. Faça um fork ou clone este repositório
2. Crie sua branch:
```bash```
git checkout -b minha-feature

3. Faça suas alterações
4. Commit:
git commit -m 'feat: nova função'

5. Push:
git push origin minha-feature

6. Abra um pull request ou avise no grupo do Trello

🧠 Participantes
Vitória Albuquerque 👩‍💻 (modelagem e EDA)

[Adicione seu nome e participação aqui]

📌 Referência do Dataset
[Pima Indians Diabetes Database – Kaggle](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)