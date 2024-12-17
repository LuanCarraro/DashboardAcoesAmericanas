import requests
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os


class alphaVantageClient:


    def __init__(self, simbolo):
        load_dotenv()
        self.apiKey = os.getenv("ALPHA_VANTAGE_API_KEY")
        self.baseUrl = "https://www.alphavantage.co/query"
        self.set_info_acao(simbolo)
        self.set_income_statement(simbolo)


    def get_info(self):
        return self.info
    
    
    def get_income_statement(self):
        return self.income_statement
    

    def set_info_acao(self, simbolo):
        urlFinal = self.baseUrl + f"?function=OVERVIEW&symbol={simbolo}&apikey={self.apiKey}"
        response = requests.get(urlFinal)
        info = response.json()
        self.info = info



        
    def set_income_statement(self, simbolo):
        urlFinal = self.baseUrl + f"?function=INCOME_STATEMENT&symbol={simbolo}&apikey={self.apiKey}"
        response = requests.get(urlFinal)
        income_statement = response.json()
        self.income_statement =  income_statement




