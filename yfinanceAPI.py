import yfinance as yf


class yfinanceClient:


    def __init__(self, simbolo):
        self.dados = yf.Ticker(simbolo)
        self.set_info_acao()
        self.set_last_interest_rate()
        self.set_income_statement()
        self.set_balance_sheet()
        
     
    def set_info_acao(self):
        self.info = self.dados.info
        
     
    def set_last_interest_rate(self):
        dados = yf.Ticker("^TNX")
        rates = dados.history(period = "1d")
        self.last_interest_rate = rates['Close'].iloc[-1]

    def set_income_statement(self):
        self.income_statement = self.dados.financials

    def set_balance_sheet(self):
        self.balance_sheet = self.dados.balance_sheet    
    
    
    def get_info_acao(self):
        return self.info
    

    def get_last_interest_rate(self):
        return self.last_interest_rate
    
    
    def get_income_statement(self):
        return self.income_statement
    
    def get_balance_sheet(self):
        return self.balance_sheet
    
    
    @staticmethod
    def get_historico_acao(simbolo, periodo):
        dados = yf.Ticker(simbolo)
        historico = dados.history(period = periodo)  
        return historico    
    

 
