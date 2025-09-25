# Projeto-IA


# Dashboard Q&A com IA (Streamlit)

Este projeto é um **exemplo de dashboard interativo** desenvolvido em **Python + Streamlit**, que simula um recurso de **Perguntas e Respostas (Q&A)** em cima de uma base de vendas fictícia.

---

##  Funcionalidades

-  **Gráficos dinâmicos** baseados em perguntas digitadas pelo usuário  
-  **Rótulos de dados** em todos os gráficos  
-  **Botão "Extrair Anexo (PDF)"** para exportar o gráfico atual em PDF  
-  **Caixa de sugestões** para feedback (exemplo de interação de usuário)  
-  Exemplo de aplicação de **IA em dashboards** (Q&A simulado)

---

## 📂 Estrutura do projeto


projeto-ia/
│── app.py # Código principal do dashboard
│── base_teste.xlsx # Base fictícia de vendas
│── requirements.txt # Dependências do projeto
│── README.md # Documentação do projeto


---

##  Como rodar localmente

1. Clone este repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/projeto-ia.git
   cd projeto-ia


2. Instale as dependências:

pip install -r requirements.txt


3. Rode o aplicativo:

streamlit run app.py


4. Abra no navegador o link:

http://localhost:8501

 Exemplos de perguntas aceitas

Total de vendas por produto

Total de vendas por região

Evolução das vendas ao longo do tempo

Quantidade vendida por produto

(O app reconhece palavras-chave da pergunta e retorna o gráfico correspondente)

 Exportação

O gráfico exibido pode ser baixado em PDF através do botão:

📎 Extrair Anexo (PDF)
