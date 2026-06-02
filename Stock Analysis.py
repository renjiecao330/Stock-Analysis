#!/usr/bin/env python
# coding: utf-8

# In[1]:


# download data of AAPL's stock price from yfinance in 4 mounths

get_ipython().system('pip install yfinance')
import yfinance as yf
import pandas as pd

data = yf.download("AAPL", start="2026-01-01", end="2026-04-13")
print(data.head(7))
#print(data.head())      first 5 line will be printed by defult


# In[2]:


# cleasing missing values

df = data[['Close']] #only keep the close price colume

print("\nMissing values: ")
print(df.isnull().sum())

df = df.dropna()  #function of cleaning these missing values

print("\nCleaned Data: ")
print(df.head())


# In[3]:


#caculate key indexes

df['Return'] = df['Close'].pct_change()  #add a new colume in dataframe as a varible colume
df = df.dropna()    #the ()is improtant otherwise this'd be the dropana method itself,not a data sheet 

print("\nData with Returns: ")
print(df.head(5))

mean_return = df['Return'].mean()
volatility = df['Return'].std()
print("\nStatistics")
print("Average Return: ",mean_return )
print("Volatility: ", volatility)


# In[6]:


#Visualization
import matplotlib.pyplot as plt

#Price Trend
plt.figure(figsize=(10,5))
plt.plot(df['Close'])   #Broken line
plt.title("AAPL price over time")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()

#Return distribution(histogram)
plt.figure(figsize=(10,5))
plt.hist(df['Return'], bins=50)
plt.title("Distribution of Daily Returns")
plt.xlabel("Return")
plt.ylabel("Frequency")
plt.savefig("AAPL price over time")
plt.savefig("Distribution of Daily Returns")

plt.show()


# In[7]:


#Multi asset analysis
#plt, sns belongs to matplotlib,plt is for basic canvas incluidng axes, title and broken line etc. 
#and sns is for more completed statics diagram such as heatmap.

import seaborn as sns
data_multi = yf.download(["AAPL", "MSFT", "TSLA"], start="2026-01-01", end="2026-04-13")['Close']
correlation = data_multi.pct_change().dropna().corr()

print("\nCorrelation Matrix: ")
print(correlation)

plt.figure(figsize=(8,6))
sns.heatmap(correlation, annot=True, cmap="coolwarm")  #annot=true:with figrues in the heatmap
plt.title("Correlation Between Stocks")
plt.savefig("Correlation Between Stocks")

plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




