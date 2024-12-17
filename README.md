# Dashboard de Ações Americanas

**Dashboard de Ações Americanas** é uma aplicação interativa desenvolvida com **Streamlit** que facilita a visualização e análise de dados de ações da Bolsa de Valores Americana. A ferramenta foi projetada para fornecer uma maneira simples e eficiente de acompanhar informações cruciais sobre as ações e suas atualizações mais recentes.

## Objetivo

O objetivo principal deste projeto é proporcionar uma interface intuitiva e dinâmica, permitindo aos usuários:

- Buscar por ações da Bolsa de Valores Americana.
- Visualizar as principais métricas financeiras e dados históricos das ações.
- Acompanhar atualizações em tempo real, como preços, dividendos, índice P/L, entre outros indicadores financeiros.

## Tecnologias Utilizadas

Este projeto foi desenvolvido em **Python**, aproveitando suas poderosas bibliotecas para análise e visualização de dados. As tecnologias e ferramentas principais incluem:

- **Streamlit**: Framework utilizado para criar interfaces interativas de maneira rápida e eficiente.
- **Pandas**: Biblioteca essencial para manipulação e análise de dados.
- **Matplotlib & Seaborn**: Bibliotecas para visualização de dados, criando gráficos e diagramas informativos.
- **yfinance**: API que fornece dados financeiros históricos e em tempo real sobre ações da bolsa.
- **AlphaVantage**: API adicional para acessar dados financeiros, como indicadores técnicos e informações sobre ações.

## Funcionalidades

- **Busca por ações**: O usuário pode pesquisar por ações específicas usando seus códigos de negociação (tickers).
- **Informações financeiras**: Exibição de métricas importantes como **P/L**, **Dividend Yield**, **WACC**, **ROA**, **ROE**, **Valor da Empresa (EV)**, **CAPM**, entre outras.
- **Gráficos e visualizações**: Visualize o desempenho histórico das ações em gráficos interativos, com possibilidade de analisar dados de diferentes períodos.
- **Atualizações em tempo real**: A aplicação busca dados financeiros atualizados para garantir que as informações exibidas estejam sempre corretas.

## Acesso Streamlit

Este é um projeto exemplo hospedado no Streamlit Cloud.

Você pode acessar o app ao vivo aqui: [Acessar App Streamlit](https://dashboardacoesamericanas-dkameghbhbhne3upfdaist.streamlit.app)


## Como Rodar o Projeto Localmente

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/LuanCarraro/DashboardAcoesAmericanas.git
   cd DashboardAcoesAmericanas
   ```

2. **Crie o Arquivo `.env`** com as seguintes variáveis:
   ```plaintext
   API_KEY=sua_chave_aqui
   ```

3. **Instale as Dependências**:
   Certifique-se de ter o Python instalado. Então, execute:
   ```bash
   pip install -r requirements.txt
   ```

4. **Rode a Aplicação**:
   ```bash
   streamlit run app.py
   ```
