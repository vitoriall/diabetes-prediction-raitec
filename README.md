# 🧠 Pré-processamento de Dados - Projeto RAITec Apoio 2025.1

Este repositório contém a primeira etapa do projeto de Machine Learning para previsão de risco de diabetes. O foco aqui é exclusivamente na **leitura e limpeza dos dados**, que será a base para as próximas etapas.

---

## 📁 Estrutura do Projeto
📦 diabetes-prediction/
├── data/ # Dataset original (não versionado)
│ └── diabetes.csv
├── src/
│ └── data_processing.py # Carregamento e limpeza dos dados
├── README.md # Este arquivo

---

## 📌 O que já foi feito

- Leitura do dataset (formato `.csv`)
- Identificação de colunas com valores zero inválidos
- Substituição de zeros por `NaN`
- Preenchimento dos dados ausentes com a média de cada coluna

---

## 🚀 Como Executar

### 1. Requisitos
Você deve ter instalado:
- Python 3.8 ou superior
- pandas
- numpy

### 2. Para rodar o script:
``` python src/data_processing.py```

### 🔎 Objetivo do Script data_processing.py
O script:

Lê o arquivo diabetes.csv da pasta /data

Corrige colunas que não podem conter zero (Glucose, BloodPressure, etc.)

Preenche os dados ausentes com a média de cada coluna

Exibe o describe() do dataframe limpo

### 🧠 Próximos passos (a serem feitos pelo grupo)

Análise Exploratória (EDA) - Amanda

Modelagem com algoritmos de ML - Camile

Avaliação dos modelos -> Bruno e Lucas
