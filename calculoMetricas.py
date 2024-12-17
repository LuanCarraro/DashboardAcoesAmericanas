
from APIs.alphaVantageAPI import alphaVantageClient
from APIs.yfinanceAPI import yfinanceClient


class calculadoraClient:
    
    # Inicia o objeto calculadoraCliente instânciando objetos das APIs
    def __init__(self, simbolo):
        self.alphaVantage = alphaVantageClient(simbolo)
        self.yf = yfinanceClient(simbolo)
        self.simbolo = simbolo

    # Determina retorno esperado do mercado através do indice SP500
    def calcularERM(self):

        # Busca os dados sobre os últimos 10 anos do indice SP500
        SP500 = yfinanceClient.get_historico_acao("^GSPC", "10y")

        # Determina a variação diária média do índice
        SP500["variacao"] = SP500["Close"].pct_change()
        media_variacao_diaria = SP500["variacao"].mean()

        # Anualiza a variação diária média
        ERm = media_variacao_diaria * 252 * 100
        return round(ERm, 2)
    

    #Calcula o CAPM da empresa escolhida
    def calcularCAPM(self):
        try:
            # Busca informações necessárias para calculo no CAPM na API yfinance
            Rf = self.yf.get_last_interest_rate()
            Beta = self.yf.get_info_acao().get("beta")
            Erm = self.calcularERM()

            # Aplica a formula do CAPM com base nos dados obtidos
            Eri =  Rf + Beta * (Erm - Rf)
            return round(Eri, 2)
        except Exception:
            return "Indisponível"
        
    

    # Calcula o WACC da empresa escolhida
    def calcularWACC(self):

        try:
           # Busca informações necessárias na API AlphaVantage e armazena-as como variaveis da calculadora para reduzir 
           # número de requisições à API
           infoAcao = self.alphaVantage.get_info()
           income_statement = self.alphaVantage.get_income_statement()
           CAPM = self.calcularCAPM()
           E = infoAcao["BookValue"]
           D = infoAcao["TotalDebt"]
           V = E + D
           Rd = income_statement["interestExpense"]
           T = infoAcao["TaxRate"]
           WACC = (CAPM * E / V) + ((D / V) * Rd * (1 - T))
           return round(WACC, 2)
        
        except Exception:
            # Caso alguma das informações não esteja disponivel, retorna a mensagem abaixo
            return "Indisponível."
    
    # Busca a razão entre preço e lucro por ação no ultimos 12 meses da empresa escolhida, através da API yfinance
    def get_trailing_PE(self):

        try:
           trailing_PE = self.yf.get_info_acao()["trailingPE"]
           return round(trailing_PE, 2)
        
        except Exception:
            # Caso alguma das informações não esteja disponivel, retorna a mensagem abaixo
            return "Indisponível."

    
    # Busca a razão entre valor de mercado da empresa escolhida e seu valor patrimonial, através da API yfinance
    def get_PB(self):

        try:
           PB = self.yf.get_info_acao()["priceToBook"]
           return round(PB, 2)
        
        except Exception:
            # Caso alguma das informações não esteja disponivel, retorna a mensagem abaixo
            return "Indisponível."   
    
    # Busca o rendimento anual dos dividendos da empresa escolhida, através da API yfinance
    def get_dividend_yield(self):

        try:
           dividendYield = self.yf.get_info_acao()["dividendYield"]
           return dividendYield
        
        except Exception:
            # Caso alguma das informações não esteja disponivel, retorna a mensagem abaixo
            return "Indisponível."
    
    # Busca o lucro por ação nos últimos 12 meses da empresa escolhida, através da API yfinance
    def get_trailing_EPS(self):

        try:
           trailing_EPS = self.yf.get_info_acao()["trailingEPS"]
           return round(trailing_EPS, 2)
        
        except Exception:
            # Caso alguma das informações não esteja disponivel, retorna a mensagem abaixo
            return "Indisponível."
    
    # Calcula o lucro da empresa para cada dolar de capital próprio investido 
    def get_ROE(self):

        try:
            net_income = self.yf.get_income_statement().loc["Net Income"].iloc[0]
            equity = self.yf.get_balance_sheet().loc["Stockholders Equity"].iloc[0]
            ROE = net_income / equity
            return round(ROE, 2)
        
        except Exception:
            # Caso alguma das informações não esteja disponivel, retorna a mensagem abaixo
            return "Indisponível."
        
    
    # Determina a razão entre dívida total e patrimonio liquido da empresa
    def get_DE_ratio(self):

        try:
           balance_sheet = self.yf.get_balance_sheet()
           equity = balance_sheet.loc["Stockholders Equity"].iloc[0]
           total_debt = balance_sheet.loc["Total Debt"].iloc[0]
           DE_ratio = total_debt / equity
           return round(DE_ratio, 2)
        
        except Exception:
            # Caso alguma das informações não esteja disponivel, retorna a mensagem abaixo
            return "Indisponível."

   # Busca o valor total da empresa, através da API yfinance
    def get_enteprise_value(self):

        try:
           enterprise_value = self.yf.get_info_acao()["enterpriseValue"]
           return enterprise_value
        
        except Exception:
            # Caso alguma das informações não esteja disponivel, retorna a mensagem abaixo
            return "Indisponível."
    
    # Determina a razão entre lucro liquido da empresa e seus ativos totais
    def get_ROA(self):

        try:
           net_income = self.yf.get_income_statement().loc["Net Income"].iloc[0]
           total_assets = self.yf.get_balance_sheet().loc["Total Assets"].iloc[0]
           ROA = (net_income / total_assets) * 100
           return round(ROA, 2)
        
        except Exception:
            # Caso alguma das informações não esteja disponivel, retorna a mensagem abaixo
            return "Indisponível."



