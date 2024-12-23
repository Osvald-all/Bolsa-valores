# Bolsa de Valores em Tempo Real

Este repositÃ³rio contÃ©m dois exemplos de programas em Python que exibem dados da bolsa de valores em tempo real, utilizando a biblioteca **Streamlit** para criar uma interface amigÃ¡vel e **yfinance** para buscar os dados.

## Recursos disponÃ­veis

1. **CÃ³digo BÃ¡sico**:
   - Exibe os preÃ§os atualizados das aÃ§Ãµes inseridas.
   - Gera grÃ¡ficos simples de fechamento.

2. **CÃ³digo Completo com Indicadores TÃ©cnicos**:
   - Exibe o preÃ§o atualizado em tempo real.
   - Gera grÃ¡ficos com indicadores tÃ©cnicos:
     - MÃ©dia MÃ³vel Simples (SMA).
     - MÃ©dia MÃ³vel Exponencial (EMA).
   - Permite configurar perÃ­odos e intervalos de anÃ¡lise.

## Como executar os cÃ³digos

### PrÃ©-requisitos
- Python 3.8 ou superior.
- Instale as bibliotecas necessÃ¡rias:
  ```bash
  pip install streamlit yfinance pandas
  ```

### Executando o programa
1. Baixe os cÃ³digos disponÃ­veis:
   - [CÃ³digo BÃ¡sico](bolsa_streamlit_basico.py)
   - [CÃ³digo Completo com Indicadores](bolsa_streamlit_completo.py)
2. No terminal, execute o comando para abrir o programa no navegador:
   ```bash
   streamlit run bolsa_streamlit_completo.py
   ```

### Interface Web
- Insira os cÃ³digos das aÃ§Ãµes (por exemplo, `AAPL, TSLA`).
- Visualize os preÃ§os e grÃ¡ficos.

## Exemplo de Uso
- Para acompanhar aÃ§Ãµes como `AAPL` (Apple) ou `TSLA` (Tesla):
  - Insira os cÃ³digos no campo de entrada.
  - Ajuste o perÃ­odo (ex.: 1 mÃªs, 6 meses) e o intervalo (ex.: 1 dia, 1 hora) na barra lateral.

## Como contribuir
Sinta-se Ã  vontade para abrir issues ou enviar pull requests para melhorias.
