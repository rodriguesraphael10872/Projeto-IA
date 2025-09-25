import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
from matplotlib.backends.backend_pdf import PdfPages

# Carrega a base
df = pd.read_excel("base_teste.xlsx")
df["Data"] = pd.to_datetime(df["Data"])

# Título
st.title(" Dashboard Q&A Simulado")
st.write("Digite uma pergunta sobre as vendas e receba a resposta em gráfico.")

# Input de pergunta
pergunta = st.text_input("Faça sua pergunta:", "")

# Sugestões
st.write(" Exemplos de perguntas:")
st.markdown("""
- Total de vendas por produto  
- Total de vendas por região  
- Evolução das vendas ao longo do tempo  
- Quantidade vendida por produto  
""")

# Normaliza
p = pergunta.lower()

# Define variáveis
fig, ax = plt.subplots(figsize=(10,6))
resumo = None

if "produto" in p and "venda" in p:
    resumo = df.groupby("Produto")["Vendas"].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10,6))
    ax.bar(resumo["Produto"], resumo["Vendas"], color="#1f77b4")
    ax.set_title("Total de vendas por produto", fontsize=14, fontweight="bold")
    ax.set_ylabel("Vendas (R$)")
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    for i, v in enumerate(resumo["Vendas"]):
        ax.text(i, v + (v * 0.02), str(v), ha='center', va='bottom', fontsize=10, fontweight="bold")

elif "região" in p and "venda" in p:
    resumo = df.groupby("Região")["Vendas"].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10,6))
    ax.bar(resumo["Região"], resumo["Vendas"], color="#ff7f0e")
    ax.set_title("Total de vendas por região", fontsize=14, fontweight="bold")
    ax.set_ylabel("Vendas (R$)")
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    for i, v in enumerate(resumo["Vendas"]):
        ax.text(i, v + (v * 0.02), str(v), ha='center', va='bottom', fontsize=10, fontweight="bold")

elif "evolução" in p or "tempo" in p or "mês" in p:
    resumo = df.groupby("Data")["Vendas"].sum().reset_index()
    fig, ax = plt.subplots(figsize=(12,6))
    ax.plot(resumo["Data"], resumo["Vendas"], marker="o", color="#2ca02c")
    ax.set_title("Evolução das vendas ao longo do tempo", fontsize=14, fontweight="bold")
    ax.set_xlabel("Data")
    ax.set_ylabel("Vendas (R$)")
    plt.xticks(rotation=45)
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    for x, y in zip(resumo["Data"], resumo["Vendas"]):
        ax.text(x, y + (y * 0.02), str(y), ha='center', fontsize=9, fontweight="bold")

elif "quantidade" in p:
    resumo = df.groupby("Produto")["Quantidade"].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10,6))
    ax.bar(resumo["Produto"], resumo["Quantidade"], color="#9467bd")
    ax.set_title("Quantidade vendida por produto", fontsize=14, fontweight="bold")
    ax.set_ylabel("Unidades")
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    for i, v in enumerate(resumo["Quantidade"]):
        ax.text(i, v + (v * 0.02), str(v), ha='center', va='bottom', fontsize=10, fontweight="bold")

else:
    st.info("👉 Digite uma das perguntas sugeridas acima para ver o resultado.")

# Renderiza gráfico
st.pyplot(fig)

# Botão de download em PDF (se houver gráfico válido)
if resumo is not None:
    pdf_bytes = io.BytesIO()
    with PdfPages(pdf_bytes) as pdf:
        pdf.savefig(fig)  # salva o gráfico exibido
        plt.close()

    st.download_button(
        label="📎 Extrair Anexo (PDF)",
        data=pdf_bytes.getvalue(),
        file_name="anexo_dashboard.pdf",
        mime="application/pdf"
    )
