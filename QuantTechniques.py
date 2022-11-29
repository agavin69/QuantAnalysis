#QuantTechniques


#MovingLinearRegression


import numpy as np
import pandas as pd
import math
import yfinance as yf
import matplotlib.pyplot as plt

symbol1 = 'AAPL'
symbol2 = 'QQQ'

# start = '2021-11-27'
# end = '2022-11-27'

start = '2018-08-01'
end = '2019-01-01'

df1 = yf.download(symbol1, start , end)
df2 = yf.download(symbol2,start,end)


avg1 = df1['Adj Close'].mean()
avg2 = df2['Adj Close'].mean()
df1['AVGS1_S1'] = avg1 - df1['Adj Close']
df1['AVGS2_S2'] = avg2 - df2['Adj Close']
df1['Average_SQ'] = df1['AVGS1_S1']**2
df1['AVG_AVG'] = df1['AVGS1_S1']*df1['AVGS2_S2']

df1.head(20)

sum_sq = df1['Average_SQ'].sum()
sum_avg = df1['AVG_AVG'].sum()
slope = sum_avg / sum_sq
intercept = avg2 - (slope*avg1)



df1['Linear_Regression'] = intercept + slope*(df1['Adj Close'])

n = 14 # number of periods
df1['Moving_Linear_Regression'] = df1['Linear_Regression'].rolling(n).mean()

df1 = df1.drop(['AVGS1_S1', 'AVGS2_S2', 'Average_SQ', 'AVG_AVG'], axis=1)
df1.head()

fig = plt.figure(figsize=(14,10))
ax1 = plt.subplot(2, 1, 1)
ax1.plot(df1['Adj Close'])
ax1.plot(df1['Linear_Regression'], label='Linear_Regression')
ax1.plot(df1['Moving_Linear_Regression'], label='Moving_Linear_Regression')
ax1.set_title('Stock '+ symbol1 +' Closing Price')
ax1.set_ylabel('Price')
ax1.legend(loc='best')

ax2 = plt.subplot(2, 1, 2)
df1['VolumePositive'] = df1['Open'] < df1['Adj Close']
colors = df1.VolumePositive.map({True: 'g', False: 'r'})
ax2.bar(df1.index, df1['Volume'], color=colors, alpha=0.4)
ax2.grid()
ax2.set_ylabel('Volume')

