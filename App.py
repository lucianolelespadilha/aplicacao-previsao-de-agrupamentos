import streamlit as st
import pandas as pd
import joblib as jl

# Carregando os objetos previamente treinados
encoder = jl.load("encoder.pkl")
scaler = jl.load("scaler.pkl")
kmeans = jl.load("kmeans.pkl")

# Título e descrição do app
st.title("Grupos de Interesse para Marketing")
st.write(
    """
    Neste projeto, aplicamos o algoritmo de clusterização K-means para identificar e prever agrupamentos de interesses de usuários, com o objetivo de direcionar campanhas de marketing de forma mais eficaz.
    Através dessa análise, conseguimos segmentar o público em bolhas de interesse, permitindo a criação de campanhas personalizadas e mais assertivas, com base nos padrões de comportamento e preferências de cada grupo.
    """
)

# Upload do arquivo CSV
up_file = st.file_uploader(
    "Escolha um arquivo CSV para realizar a previsão", type=["csv"]
)


def processar_prever(df):
    # Etapa 1: Codificação da variável categórica "sexo"
    # O encoder já foi treinado com os dados originais.
    # Aqui ele transforma os dados da coluna "sexo" em formato numérico (ex: one-hot encoding).
    encoded_sexo = encoder.transform(df[["sexo"]])

    # Converte o resultado da codificação em um DataFrame com nomes de colunas adequados.
    encoded_df = pd.DataFrame(
        encoded_sexo, columns=encoder.get_feature_names_out(["sexo"])
    )

    # Etapa 2: Substitui a coluna original "sexo" pelas colunas codificadas.
    # Remove "sexo" do DataFrame original e concatena com as novas colunas codificadas.
    dados = pd.concat([df.drop(columns=["sexo"]), encoded_df], axis=1)

    # Etapa 3: Aplica o escalonamento aos dados (ex: normalização ou padronização).
    # Utiliza o mesmo scaler (ex: StandardScaler) usado durante o treinamento do modelo.
    dados_escalados = scaler.transform(dados)

    # Etapa 4: Realiza a previsão do cluster usando o modelo kmeans treinado anteriormente.
    cluster = kmeans.predict(dados_escalados)

    # Etapa 5: Retorna o número do cluster previsto para os dados informados.
    return cluster


if up_file is not None:

    st.write(
        """
          ### Descrição dos Grupos:
            - **Grupo 0** é focado em um público jovem com forte interesse em moda, música e aparência.
            - **Grupo 1** está muito associado a esportes, especialmente futebol americano, basquete e atividades culturais como banda e rock.
            - **Grupo 2** é mais equilibrado, com interesses em música, dança, e moda.
        """
    )
    
    df = pd.read_csv(up_file)
    cluster = processar_prever(df)
    df.insert(0, "grupos", cluster)

    st.write("Visualização dos resultados (10 primeiros registros):")
    st.write(df.head(10))

    csv = df.to_csv(index=False)
    st.download_button(
        label="Baixar resultados",
        data=csv,
        file_name="Grupos_interesse.csv",
        mime="text/csv",
    )
