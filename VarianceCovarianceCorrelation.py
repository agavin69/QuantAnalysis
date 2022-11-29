#Variance, Covariance, Correlation

import math
import numpy as np
import yfinance as yf

symbol = 'AMD'
market = '^GSPC'

start = '2018-01-01'
end = '2019-01-01'

dataset = yf.download(symbol, start, end)['Adj Close']
benchmark = yf.download(market, start, end)['Adj Close']

dataset.head()

variance = ((dataset - dataset.mean())**2).sum() / len(dataset)



covariance = ((dataset - dataset.mean()) * (dataset - dataset.mean())).sum() / (len(dataset) - 1)



covariance2 = ((dataset - dataset.mean()) * (benchmark - benchmark.mean())).sum() / (len(dataset) - 1)



print("The Covariance for " + symbol + ":", covariance)

top = ((dataset - dataset.mean()) * (benchmark - benchmark.mean())).sum()
bottom = np.sqrt((((dataset-dataset.mean())**2).sum()) * (((benchmark - benchmark.mean())**2).sum()))

correlationCoeff = top / bottom

print(correlationCoeff)
r_square = correlationCoeff**2




