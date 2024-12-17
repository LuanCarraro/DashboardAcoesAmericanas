import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def checkSimbolo(simbolo):
    if "." in simbolo:
        return False
    else:
        return True

def gerarGrafico(dados):
    plt.figure(figsize=(10,6))
    sns.lineplot(dados, x = dados.index, y = "Close")
    plt.ylim(dados["Close"].min() - 5, dados["Close"].max() + 5)
    plt.xticks(rotation = 45, ha='right')
    plt.xlabel('Data', color='white')
    plt.ylabel('Preço de Fechamento', color='white')
    plt.gcf().patch.set_facecolor('#0E1117')  
    plt.gca().set_facecolor('#0E1117')
    plt.tick_params(axis='both', colors='white')
    plt.gca().spines['top'].set_color('white')    
    plt.gca().spines['right'].set_color('white')  
    plt.gca().spines['left'].set_color('white')   
    plt.gca().spines['bottom'].set_color('white')  
    st.pyplot(plt)