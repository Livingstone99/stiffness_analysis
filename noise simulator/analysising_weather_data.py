import csv
from datetime import datetime
floatt = []
with open('google_stock_data.csv', 'r') as data:
    readd = csv.reader(data)
    header = next(readd)
    # readd = csv.DictReader(data)

    for row in readd:
        print('do it',row[0]+'vaucha')
        date = datetime.strptime(row[0], '%m/%d/%Y')
        open_price = float(row[1])
        high = float(row[2])
        low = float(row[3])
        close = float(row[4])
        volume = float(row[5])
        adj_close = float(row[6])
        floatt.append([date, open_price, high, low, volume, adj_close])

print(floatt[:3])
# rang = ax[:4]
# print(ax)
year = []
month = []
OPEN = []
for i in range(len(floatt)):
    #reducung the date string to only year e.g '2004'
    year.append((str(floatt[i][0])[:4]))
    #REVERSING THE LIST TO START FROM THE 2004
    month.append((str(floatt[i][0])[5:7]))

year = (list(reversed(year)))
month = (list(reversed(month)))


# this code is capable of getting the average of
# yesrly figure :))
r = -1
i = -1
yearly = []
yearly_data = []
yearly_sum = []
month = ['01','02','03','04','05','06','07','08','09','10','11','12']
print(str(floatt[0][0])[5:7])
w = 1
n = -1
m = -1
for w in floatt:
    n +=1
    m +=1
    yearly.append([])
    if (str(floatt[n][0])[:4]) == [str(i) for i in range(2004,2014)]:
        yearly[m].append(str(floatt[n][1]))
        print('listing',w)
        yearly_data.append(w)
        # print('this is it', str(floatt[n][1]))
yearly_data = list(reversed(yearly_data))
print('ok',str(yearly_data[0][0])[5:7])
print('ok man',len(yearly_data))

# turns each member of the list to a float
for i in yearly:
    yearly_sum.append(float(i))

yearly_average = sum((yearly_sum))/len(yearly_sum)
print('yearly average', yearly_average)
##
a = -1
monthly_data = []
print('monthing', len(yearly_data))
dd= [str(k) for k in month]
for i in yearly_data:
    a += 1
    monthly_data.append([])
    for dd in month:
        if str(yearly_data[a][0])[5:7] == dd:
            print((str(floatt[a][0])[5:7]))
            monthly_data[a].append(i)
print('hello :)', monthly_data)
print('hello :)', len(monthly_data))
            # print(sum(monthly_data[a]))




