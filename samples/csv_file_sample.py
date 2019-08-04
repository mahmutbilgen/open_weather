'''
Printing CSV file
Sample File : Google Stock Market Data - google_stock_data.csv
'''



path="./google_stock_data.csv"

lines = [line for line in open(path)]

# print(lines[0])

# print(lines[1])

dataset  = [line.strip().split(',') for line in open(path)]
print(dataset[0])
print(dataset[1][0])



