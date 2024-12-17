
import streamlit as st
import util 
from calculoMetricas import calculadoraClient
from yfinanceAPI import yfinanceClient


st.set_page_config(page_title="Dashboard Financeiro", layout="wide")

# Adicionando Titulo da pagina
st.title("📊 Dashboard de Ações")
st.write("Análise informações de Ações da bolsa de valores americana")

# Recebendo o input do usuário acerca do simbolo requerido
symbol = st.text_input("Insira o simbolo da ação (e.g., AAPL para Apple)", placeholder="Digite o simbolo da ação...")

# Validar processar simbolo da ação
if symbol:
    # Inicializa API yfinance e Calculadora
    yf_client = yfinanceClient(symbol)
    calc_client = calculadoraClient(symbol)

    # Busca informações sobre a ação
    if util.checkSimbolo(symbol):
        st.write("## Stock Information")
        info = yf_client.get_info_acao()
        
        # Determina layout das colunas
        col1, col2 = st.columns([2, 3])  

        with col1:
            st.subheader("Métrica Principais")
            st.metric(label="Nome da Empresa", value=info.get('longName', 'N/A'))
            st.metric(label="Beta", value=info.get('beta', 'N/A'))
            st.metric(label="Capitalização de Mercado", value=f"${info.get('marketCap', 'N/A'):,}")
            st.metric(label="Índice P/L", value=info.get('trailingPE', 'N/A'))
            st.metric(label = "Índice P/VPA", value = calc_client.get_PB())
            

        with col2:
            # Seção do Gráfico
            st.subheader("Histórico de preço da ação")
            period = st.selectbox("Selecione o Periodo", ["1d", "5d", "1mo", "6mo", "1y", "5y", "max"], index=4)
            history = yf_client.get_historico_acao(symbol, period)

            # Verifica se há informações dísponiveis sobre o historico da ação
            if not history.empty:
                st.line_chart(history['Close'])
            else:
                st.error("Dados indisponíveis para esta ação e período")

        # Define layout das colunas exibidas abaixo da linha do gráfico        

        col3, col4, col5, col6 = st.columns([1,1,2,1])

        with col3:
            st.metric(label = "WACC", value = calc_client.calcularWACC())
            st.metric(label = "Dividend Yield", value = calc_client.get_dividend_yield())

        with col4:
            st.metric(label = "ROA", value = calc_client.get_ROA())
            st.metric(label = "ROE", value = calc_client.get_ROE())

        with col5:
            st.metric(label = "Valor da Empresa", value = f"US$ {calc_client.get_enteprise_value():,.2f}")
            st.metric(label = "Índice de Endividamento", value = calc_client.get_DE_ratio())

        with col6:
            st.metric(label = "CAPM", value = calc_client.calcularCAPM())
            st.metric(label = "ERM", value = calc_client.calcularERM())


             

    else:
        st.error("Simbolo de ação inválido. Por favor, tente de novo.")
