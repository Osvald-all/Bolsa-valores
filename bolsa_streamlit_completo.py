
import streamlit as st
import yfinance as yf
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Bolsa de Valores em Tempo Real", layout="wide")

# Cabeçalho
st.title("Bolsa de Valores em Tempo Real")
st.subheader("Acompanhe os preços atualizados e indicadores técnicos das ações.")

# Entrada de símbolos de ações
symbols = st.text_input("Digite os códigos das ações separados por vírgula (ex: AAPL, MSFT, TSLA):", "AAPL, MSFT, TSLA")

# Seleção de período e intervalo
st.sidebar.title("Configurações de Análise")
period = st.sidebar.selectbox("Selecione o período:", ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"], index=2)
interval = st.sidebar.selectbox("Selecione o intervalo de tempo:", ["1m", "2m", "5m", "15m", "30m", "1h", "1d", "1wk", "1mo"], index=6)

# Função para calcular SMA e EMA
def calculate_indicators(data, window):
    data[f"SMA_{window}"] = data['Close'].rolling(window=window).mean()
    data[f"EMA_{window}"] = data['Close'].ewm(span=window, adjust=False).mean()
    return data

if symbols:
    try:
        # Transformando os símbolos em lista
        symbols_list = [s.strip().upper() for s in symbols.split(",")]

        # Obtendo os dados em tempo real
        st.sidebar.info("Carregando dados...")
        data = yf.download(tickers=" ".join(symbols_list), period=period, interval=interval, group_by="ticker", progress=False)

        # Exibindo os preços e gráficos
        st.subheader("Cotações e Indicadores Técnicos:")
        for symbol in symbols_list:
            if symbol in data.columns.levels[0]:
                st.write(f"### {symbol}")

                # Último preço
                last_price = data[symbol]['Close'].iloc[-1]
                st.metric(label=f"{symbol} - Último Preço", value=f"${last_price:.2f}")

                # Indicadores técnicos
                st.write(f"#### Gráficos com Indicadores Técnicos - {symbol}")
                stock_data = data[symbol].dropna()
                stock_data = calculate_indicators(stock_data, window=20)  # Calcula SMA e EMA

                # Exibindo gráfico
                chart_data = stock_data[['Close', 'SMA_20', 'EMA_20']]
                st.line_chart(chart_data)

    except Exception as e:
        st.error(f"Erro ao buscar os dados: {e}")
