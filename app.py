import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
from matplotlib.backends.backend_pdf import PdfPages

# Carrega a base
df = pd.read_excel("base_teste.xlsx")
df["Data"] = pd.to_datetime(df["Data"])

# Título
st.title("🔎 Dashboard Q&A Simulado")
st.write("Digite uma pergunta sobre as vendas e receba a resposta em gráfico.")

# Input de pergunta
pergunta = st.text_input("Faça sua pergunta:", "")

# Sugestões
st.write("💡 Exemplos de perguntas:")
st.markdown("""
- Total de vendas por produto  
- Total de vendas por região  
- Evolução das vendas ao longo do tempo  
- Quantidade vendida por produto  
""")

# Normaliza
p = pergunta.lower()

# Inicia figura
fig, ax = plt.subplots(figsize=(8,5))
resumo = None  # guarda dados para exportação

if "produto" in p and "venda" in p:
    resumo = df.groupby("Produto")["Vendas"].sum().reset_index()
    ax.bar(resumo["Produto"], resumo["Vendas"])
    ax.set_title("Total de vendas por produto")
    ax.set_ylabel("Vendas (R$)")
    for i, v in enumerate(resumo["Vendas"]):
        ax.text(i, v + 5000, str(v), ha='center', va='bottom', fontsize=9)

elif "região" in p and "venda" in p:
    resumo = df.groupby("Região")["Vendas"].sum().reset_index()
    ax.bar(resumo["Região"], resumo["Vendas"])
    ax.set_title("Total de vendas por região")
    ax.set_ylabel("Vendas (R$)")
    for i, v in enumerate(resumo["Vendas"]):
        ax.text(i, v + 5000, str(v), ha='center', va='bottom', fontsize=9)

elif "evolução" in p or "tempo" in p or "mês" in p:
    resumo = df.groupby("Data")["Vendas"].sum().reset_index()
    ax.plot(resumo["Data"], resumo["Vendas"], marker="o")
    ax.set_title("Evolução das vendas ao longo do tempo")
    ax.set_xlabel("Data")
    ax.set_ylabel("Vendas (R$)")
    plt.xticks(rotation=45)
    for x, y in zip(resumo["Data"], resumo["Vendas"]):
        ax.text(x, y + 5000, str(y), ha='center', fontsize=8)

elif "quantidade" in p:
    resumo = df.groupby("Produto")["Quantidade"].sum().reset_index()
    ax.bar(resumo["Produto"], resumo["Quantidade"])
    ax.set_title("Quantidade vendida por produto")
    ax.set_ylabel("Unidades")
    for i, v in enumerate(resumo["Quantidade"]):
        ax.text(i, v + 5, str(v), ha='center', va='bottom', fontsize=9)

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
