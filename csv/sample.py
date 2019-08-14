'''
sample data file:
1/2/2018,5,8,red
1/3/2018,5,2,green
1/4/2018,9,1,blue
'''
import csv

with open("example.csv") as data_file:
    csv_reader = csv.reader(data_file, delimiter=',')

    dates = []
    colors = []
    for line in csv_reader:
        color = line[3]
        date = line[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)

    whatcolor = input('What color do you wish to know')
    coldex = colors.index(whatColor)

    theDate = dates[coldex]

    print('The date of', whatColor, 'is')


# with open("example.csv") as data_file:
#     csv_reader = csv.reader(data_file, delimiter=',')

#     dates = []
#     colors = []
#     for line in csv_reader:
#         color = line[3]
#         date = line[0]

#         dates.append(date)
#         colors.append(color)

#     print(dates)
#     print(colors)

'''
Output:
['1/2/2018', '1/3/2018', '1/4/2018']
['red', 'green', 'blue']
'''


# with open("example.csv") as data_file:
#     csv_reader = csv.reader(data_file, delimiter=',')

#     for line in csv_reader:
#         print(line)

'''
output:
['1/2/2018', '5', '8', 'red']
['1/3/2018', '5', '2', 'green']
['1/4/2018', '9', '1', 'blue']

'''
