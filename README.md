# aplicacao-previsao-de-agrupamentos
# 🔍 Aplicação de Previsão de Agrupamentos com K-Means

Este projeto utiliza **aprendizado não supervisionado** — especificamente o algoritmo **K-Means** — para agrupar usuários com base em características como tempo de navegação, idade, escolaridade, entre outros. A finalidade é **identificar perfis de interesse** e permitir campanhas de marketing **mais personalizadas e eficazes**.

---

## 🎯 Objetivo

Agrupar consumidores com características semelhantes para entender **tendências de comportamento** e planejar ações de marketing segmentadas. Através dos clusters, é possível criar campanhas que se conectam melhor com o público-alvo, aumentando conversão e engajamento.

---

## 🧠 Tecnologias Utilizadas

- **Python 3**
- **Pandas**, **NumPy**, **Scikit-learn**
- **KMeans** (clusterização)
- **OneHotEncoder**, **MinMaxScaler**
- **Streamlit** (para interface web)
- **Joblib** (salvar/carregar modelos)

---

## 🖥️ Aplicação Web Interativa

A aplicação permite que usuários carreguem arquivos `.csv` com dados e vejam **em tempo real** a qual cluster cada novo dado pertence.

### Funcionalidades:
- Upload de novos dados para previsão
- Visualização de grupos (clusters) atribuídos
- Interface simples com **Streamlit**

---

## 🚀 Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/lucianolelespadilha/aplicacao-previsao-de-agrupamentos.git
cd aplicacao-previsao-de-agrupamentos
