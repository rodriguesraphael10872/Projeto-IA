import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carrega a base
df = pd.read_excel("base_teste.xlsx")
df["Data"] = pd.to_datetime(df["Data"])

st.title("🔎 Dashboard Q&A Simulado")
st.write("Digite uma pergunta sobre as vendas e receba a resposta em gráfico.")

# Input de pergunta
pergunta = st.text_input("Faça sua pergunta:", "")

# Normaliza para lower
p = pergunta.lower()

fig, ax = plt.subplots(figsize=(8,5))

if "produto" in p and "venda" in p:
    resumo = df.groupby("Produto")["Vendas"].sum().reset_index()
    ax.bar(resumo["Produto"], resumo["Vendas"])
    ax.set_title("Total de vendas por produto")

elif "região" in p and "venda" in p:
    resumo = df.groupby("Região")["Vendas"].sum().reset_index()
    ax.bar(resumo["Região"], resumo["Vendas"])
    ax.set_title("Total de vendas por região")

elif "evolução" in p or "tempo" in p or "mês" in p:
    resumo = df.groupby("Data")["Vendas"].sum().reset_index()
    ax.plot(resumo["Data"], resumo["Vendas"], marker="o")
    ax.set_title("Evolução das vendas ao longo do tempo")
    ax.set_xlabel("Data")
    ax.set_ylabel("Vendas (R$)")

elif "quantidade" in p:
    resumo = df.groupby("Produto")["Quantidade"].sum().reset_index()
    ax.bar(resumo["Produto"], resumo["Quantidade"])
    ax.set_title("Quantidade vendida por produto")

else:
    st.info("Digite algo como: 'total de vendas por produto', 'total de vendas por região', 'evolução das vendas ao longo do tempo'...")

st.pyplot(fig)
