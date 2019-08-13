'''
Printing CSV file
Sample File : Google Stock Market Data - google_stock_data.csv

You can download a CSV containing the first 10 years of Google stock data here:
https://goo.gl/3zaUlD

'''
import csv
from  datetime import datetime


path="./google_stock_data.csv"
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader)  # The first line is the header

data = []

for row in reader:
    print
    #row =  ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1])
    high = float(row[2])
    low = float(row[3])
    close_price = float(row[4])
    volume = int (row[5])
    adj_volume = float (row[6])
    data.append([date,open_price,high, low, close_price, volume, adj_volume])

print(data[0])

## Compute and store daily stock returns

returns_path = "./google_returns.csv"
file = open(returns_path,'w')
writer = csv.writer(file)
writer.writerow(["Date","Return"])

for i in range(len(data) - 1):
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]
    yesterdays_row = data[i+1]
    yesterdays_price = yesterdays_row[-1]

    daily_return = (todays_price - yesterdays_price) / yesterdays_price
    formatted_date = todays_date.strftime('%m/%d/%Y')
    writer.writerow([formatted_date,daily_return])




