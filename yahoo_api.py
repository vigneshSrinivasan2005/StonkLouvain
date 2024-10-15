import yfinance as yf
import pandas as pd
# Function to retrieve data for a list of companies
def get_company_data(tickers):
    data = {}
    for i in range(len(tickers)):
        ticker = tickers[i]
        company = yf.Ticker(ticker)
        data[ticker] = company.history(period="1y")
    return data

# get List of company tickers
file = open("all_tickers.txt", "r")
tickers = file.read().split()
print(tickers)
company_data = get_company_data(tickers)

file = open("all_tickers.txt", "r")
df  = pd.DataFrame(columns=["Date"])
dates = []
example = yf.Ticker(tickers[0])
dates = example.history(period="1y").index
df["Date"] = dates

# Print the data for each company
for ticker, data in company_data.items():
    tickerData = []
    for i in range(len(data)):
        tickerData.append((data["Close"][i]-data["Open"][i])/data["Open"][i])
    print(len(tickerData))
    if(len(tickerData) >= 251):
        df[f"{ticker}"] = tickerData
df.to_csv("2023-2024StonkLouvainData.csv",index=False)
print(df)