#!/usr/bin/env python
# coding: utf-8

# # IV. Financial Data Visualization Using Python
# 

# ## Collecting Stock Price Data:

# In[1]:


get_ipython().system('pip install yfinance')


# In[70]:


import yfinance as yf

# Define the stock symbol
stock_symbol = "RY.TO"

# Define the date range
start_date = "2023-01-01"
end_date = "2024-02-29"

# Download historical stock data
RBC_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Print the stock data
RBC_data.head()


# ## Analyzing Stock Price Data:

#  1. Plot a line graph to show the adjusted close price change in 2024

# In[67]:


RBC_2024=RBC_data.iloc[range(250,290)]
RBC_2024.head()


# In[42]:


import matplotlib.pyplot as plt

# Create a line plot of the closing price
plt.plot(RBC_2024['Adj Close'])

# Add axis labels and a title
plt.xlabel('Date')
plt.ylabel('Adj Close Price')
plt.title('RBC' + ''+' Adj Close Price')

# Rotate the x-axis labels to be vertical
plt.xticks(rotation=90)

# Show the plot
plt.show()


#  2. Plot the daily returns of the stock price data for 2024
# 

# In[43]:


daily_returns = RBC_2024['Adj Close'].pct_change()
daily_returns.head()


# In[44]:


import matplotlib.pyplot as plt

# Prepare graph size
fig = plt.figure(figsize=(10, 8)) 
ax = fig.add_subplot(111)

# Plot the daily returns data on the subplot
ax.plot(daily_returns) 

# Set the axis labels and title
ax.set_xlabel("Date") 
ax.set_ylabel("Percent") 
ax.set_title("Daily returns data") 

# Show the plot
plt.show()


# 3. Plot the cumulative daily return of the stock price data for 2024

# In[45]:


cumulative_returns = (daily_returns + 1).cumprod()

# Prepare graph size
fig = plt.figure(figsize=(10, 8))  
ax = fig.add_subplot(111)

# Plot the cumulative returns data
ax.plot(cumulative_returns) 
ax.set_xlabel("Date") 
ax.set_ylabel("Investment") 
ax.set_title("Cumulative daily returns data")    
plt.show()


# 4. Calculate the volatility of the stock price data for that month.

# In[46]:


# Define the minimum of periods to consider 
min_periods = 5 
import numpy as np
# Calculate the volatility 
vol = daily_returns.rolling(min_periods).std() * np.sqrt(min_periods) 

# plot volatility 
fig = plt.figure(figsize=(10, 8)) 
ax = fig.add_subplot(111)
ax.plot(vol, label='Adj Close')
ax.set_xlabel("Date") 
ax.set_ylabel("Volatility") 
ax.set_title("Volatility Graph") 
ax.legend()   
plt.show()


# ## Moving Average of RBC's stock price 

# In[59]:


import yfinance as yf

# Define the stock symbol
stock_symbol = "RY.TO"

# Define the date range
start_date = "2019-01-01"
end_date = "2024-02-29"

# Download historical stock data
RBC_data_5YR = yf.download(stock_symbol, start=start_date, end=end_date)

# Print the stock data
RBC_data_5YR .head()


# In[60]:


# 100 days
adj_close = RBC_data_5YR ['Adj Close']
mov_avg = adj_close.rolling(window=100).mean()


# 2.Calculate the moving average for the short-term and long-term window periods

# In[61]:


# Prepare graph size
fig = plt.figure(figsize=(10, 8)) 
ax = fig.add_subplot(111)

# Plot the stock price and the moving average
ax.plot(adj_close, label='Adj Close')
ax.plot(mov_avg, label='100 Days Moving Average') 

# Add axis labels, title and legend
ax.set_xlabel("Date") 
ax.set_ylabel("Window") 
ax.set_title("Moving Average") 
ax.legend()   

# Show the plot
plt.show()


# # Dividend

# Shareholders benefit from a company's wealth through dividends in the form of additional shares. Dividend payments encourage shareholders to keep investing in the company. Companies issue dividends based on the number of shares each shareholder holds. For example, if the company issues a 20% dividend, each shareholder's stock holdings will increase by 20%.The dividend yield can be calculated by dividing the annual dividend by the current stock price. 

# In[65]:


stock_price = 132.617325#adj close price in 2023 last day 
annual_dividend = 5.34 #based on the 2023 anual report

dividend_yield = annual_dividend/stock_price * 100

print("Divident Yield Percentage: " + str(dividend_yield) + "%")


# In[ ]:




