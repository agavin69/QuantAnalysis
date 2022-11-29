#Black Scholes Equation

import numpy as np
from scipy.stats import norm
from matplotlib import pyplot as plt
from math import log, sqrt, pi, exp
import pandas as pd
from pandas import DataFrame
import pandas_datareader.data as web
import datetime as dt
import pandas_datareader.data as web


N = norm.cdf

def d1(S, K, T, r, sigma):
    return (np.log(S/K) + (r + sigma**2/2)*T) / sigma*np.sqrt(T)

def d2(S, K, T, r, sigma):
    return d1(S, K, T, r, sigma) - sigma* np.sqrt(T)

def BS_CALL(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * N(d1) - K * np.exp(-r*T)* N(d2)

def BS_PUT(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma* np.sqrt(T)
    return K*np.exp(-r*T)*N(-d2) - S*N(-d1)


def delta_call(S, K, T ,r, sigma):
    return N(d1(S, K, T, r, sigma))

def delta_put(S,K,T,r,sigma):
    return - N(-d1(S, K, T, r, sigma))


S = 100
K = 100
T = 1
r = 0.00
sigma = 0.25

prices = np.arange(1, 250,1)

deltas_c = delta_call(prices, K, T, r, sigma)
plt.plot(prices, deltas_c, label='Delta Call')
plt.xlabel('$S_0$')
plt.ylabel('Delta')
plt.title('Stock Price Effect on Delta for Calls/Puts' )
plt.axvline(K, color='black', linestyle='dashed', linewidth=2,label="Strike")
plt.legend()
plt.show()

start = dt.datetime(2012,1,1)    
end =dt.datetime(2022,10,1) 
symbol = 'AAPL' ###using Apple as an example
source = 'yahoo'
data = web.DataReader(symbol, source, start, end)
data['change'] = data['Adj Close'].pct_change()
data['rolling_sigma'] = data['change'].rolling(20).std() * np.sqrt(255)


data.rolling_sigma.plot()
plt.ylabel('$\sigma$')
plt.title('AAPL Rolling Volatility')
plt.show()



