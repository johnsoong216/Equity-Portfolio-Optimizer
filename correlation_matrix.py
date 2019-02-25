"""
This is a class that generates a correlation matrix of stock prices
"""

import quandl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import pandas_datareader as dr



sp500 = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
                                 header=0)[0]
sp500ticker = sp500['Symbol'].values

def quandl_fetch(ticker_list:list, start: str, end: str) -> None:
    ticker_string = []
    for i in range(len(ticker_list)):
        ticker_string.append('WIKI/' + str(ticker_list[i]) + '.4')
    
    for i in range(len(ticker_list)):
        df[i] = quandl.get(quandlsp500[i], authtoken = '1RXW4dVEsT3LTuz6Byaz', start_date = start, end_date = end
                           , transformation = 'rdiff')


    




# df= Quandl.get('WIKI/FB', authtoken = '1RXW4dVEsT3LTuz6Byaz')

