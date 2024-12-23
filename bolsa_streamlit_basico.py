
import streamlit as st
import yfinance as yf
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Bolsa de Valores em Tempo Real", layout="wide")

# Cabeçalho
st.title("Bolsa de Valores em Tempo Real")
st.subheader("Acompanhe os preços atualizados das ações.")

# Entrada de símbolos de ações
symbols = st.text_input("Digite os códigos das ações separados por vírgula (ex: AAPL, MSFT, TSLA):", "AAPL, MSFT, TSLA")

if symbols:
    try:
        # Transformando os símbolos em lista
        symbols_list = [s.strip().upper() for s in symbols.split(",")]

        # Obtendo os dados em tempo real
        data = yf.download(tickers=" ".join(symbols_list), period="1d", interval="1m", group_by="ticker", progress=False)

        # Exibindo os preços
        st.subheader("Cotações em Tempo Real:")
        for symbol in symbols_list:
            if symbol in data.columns.levels[0]:
                last_price = data[symbol]['Close'].iloc[-1]
                st.metric(label=f"{symbol} - Último Preço", value=f"${last_price:.2f}")

        # Gráfico
        st.subheader("Gráficos das Ações:")
        for symbol in symbols_list:
            if symbol in data.columns.levels[0]:
                st.write(f"Gráfico para {symbol}:")
                chart_data = data[symbol]['Close']
                st.line_chart(chart_data)
    except Exception as e:
        st.error(f"Erro ao buscar os dados: {e}")
