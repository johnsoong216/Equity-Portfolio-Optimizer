"""
This is a function that generates a correlation matrix between different stocks
"""

import quandl
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from itertools import combinations


"""
Read SP500 data
"""

sp500 = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
                                 header = 0)[0]
sp500ticker = sp500['Symbol'].values

def cor_matrix(ticker_list:list, start: str, end: str) -> pd.DataFrame:
    ticker_string = []
    for i in range(len(ticker_list)):
        ticker_string.append('WIKI/' + str(ticker_list[i]) + '.4')
    df = quandl.get(ticker_string, authtoken = '1RXW4dVEsT3LTuz6Byaz', start_date = start, end_date = end
                           , transformation = 'rdiff')
    matrix = df.to_numpy().T
    matrix[np.isnan(matrix)] = 0
    corrmatrix = np.corrcoef(matrix)
    corrmatrix = pd.DataFrame(corrmatrix, columns = ticker_list, index = ticker_list)
    return corrmatrix



#Example with Visualization
corr = cor_matrix(['FB','T','F', 'MMM', 'MSFT','PM'], '2015-10-01', '2015-10-31')
sns.heatmap(corr, square = True, cmap = sns.color_palette("Blues"))
plt.show()
