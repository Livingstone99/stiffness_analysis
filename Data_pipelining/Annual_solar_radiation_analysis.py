import csv
import  math
import statistics
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
basket = []
# def running(monthing):
## THIS CODE OPENS THE EXCEL FILE IN PYTHON
with open('peter_updated_weather.csv', 'r') as data:
    readd = csv.reader(data)
    header = next(readd)
    for row in readd:
        year = int(row[2])
        monthly = int(row[3])
        daily = int(row[4])
        max_temp = float(row[8])
        min_temp = float(row[9])
        basket.append([year, monthly,daily, max_temp, min_temp])
# print(basket[:10], len(basket))
t = -1
h = -1
yearly_data = [[],[],[],[],[]]
## THIS FOR LOOP ADDS EACH YEARLY DATA IN THE LIST IN YEARLY_DATA
## THIS RUNS ACCORDING TO THE NUMBER OF YEAR
for i in basket:
    t +=1
    if basket[t][0] == 2015:
        yearly_data[0].append(i)
t =-1
for w16 in basket:
    t +=1
    if basket[t][0] == 2016:
        yearly_data[1].append(w16)
t = -1
for i in basket:
    t +=1
    if basket[t][0] == 2017:
        yearly_data[2].append(i)
t = -1
for i in basket:
    t +=1
    if basket[t][0] == 2018:
        yearly_data[3].append(i)
t = -1
for i in basket:
    t +=1
    if basket[t][0] == 2019:
        yearly_data[4].append(i)
maximum_temperature1 = []
maximum_temperature1_total = [[],[],[],[],[]]
min_temp1 = []
min_temp1_total = [[],[],[],[],[]]
## THIS FOR LOOP COLLECTS AND STORES THE MONTHLY DATA
## AND CALCULATES THE MONTHLY AVERAGE OF THE DATA
## USING STATISTICS IN-BUILT FUNCTION
## FOR 2015
for mm in range(yearly_data[0][len(yearly_data[0])-1][1]):
    maximum_temperature1.append([])
    min_temp1.append([])
    mm1 = mm + 1
    t = -1
    for i in yearly_data[0]:
        t +=1
        if yearly_data[0][t][1] == mm1:
            maximum_temperature1[mm].append(i[3])
            min_temp1[mm].append(i[4])
    maximum_temperature1_total[0].append(statistics.mean(maximum_temperature1[mm]))
    min_temp1_total[0].append(statistics.mean(min_temp1[mm]))
print('max',maximum_temperature1_total[0],'\nmin',min_temp1_total[0])
maximum_temperature1.clear()
min_temp1.clear()
## FOR 2016
mm1 = 0
for mm in range(yearly_data[1][len(yearly_data[1])-1][1]):
    maximum_temperature1.append([])
    min_temp1.append([])
    mm1 = mm + 1
    t = -1
    for i in yearly_data[1]:
        t +=1
        if yearly_data[1][t][1] == mm1:
            maximum_temperature1[mm].append(i[3])
            min_temp1[mm].append(i[4])
    maximum_temperature1_total[1].append(statistics.mean(maximum_temperature1[mm]))
    min_temp1_total[1].append(statistics.mean(min_temp1[mm]))
print('max',maximum_temperature1_total[1],'\nmin',min_temp1_total[1])

maximum_temperature1.clear()
min_temp1.clear()
## FOR 2017
for mm in range(yearly_data[2][len(yearly_data[2])-1][1]):
    maximum_temperature1.append([])
    min_temp1.append([])
    mm1 = mm + 1
    t = -1
    for i in yearly_data[2]:
        t +=1
        if yearly_data[2][t][1] == mm1:
            maximum_temperature1[mm].append(i[3])
            min_temp1[mm].append(i[4])
    maximum_temperature1_total[2].append(statistics.mean(maximum_temperature1[mm]))
    min_temp1_total[2].append(statistics.mean(min_temp1[mm]))
print('max',maximum_temperature1_total[2],'\nmin',min_temp1_total[2])

maximum_temperature1.clear()
min_temp1.clear()
## FOR 2018
for mm in range(yearly_data[3][len(yearly_data[3])-1][1]):
    maximum_temperature1.append([])
    min_temp1.append([])
    mm1 = mm + 1
    t = -1
    for i in yearly_data[3]:
        t +=1
        if yearly_data[3][t][1] == mm1:
            maximum_temperature1[mm].append(i[3])
            min_temp1[mm].append(i[4])
    maximum_temperature1_total[3].append(statistics.mean(maximum_temperature1[mm]))
    min_temp1_total[3].append(statistics.mean(min_temp1[mm]))
print('max',maximum_temperature1_total[3],'\nmin',min_temp1_total[3])

## FOR 2019
maximum_temperature1.clear()
min_temp1.clear()
for mm in range(yearly_data[4][len(yearly_data[4])-1][1]):
    maximum_temperature1.append([])
    min_temp1.append([])
    mm1 = mm + 1
    t = -1
    for i in yearly_data[4]:
        t +=1
        if yearly_data[4][t][1] == mm1:
            maximum_temperature1[mm].append(i[3])
            min_temp1[mm].append(i[4])
    maximum_temperature1_total[4].append(statistics.mean(maximum_temperature1[mm]))
    min_temp1_total[4].append(statistics.mean(min_temp1[mm]))
print('max',maximum_temperature1_total[4],'\nmin',min_temp1_total[4])

# #
b = 0
snn = []
snn_leap_year = []
snn_last_year = []
month_day = [31,28,31,30,31,30,31,31,30,31,30,31]
month_leap_day = [31,29,31,30,31,30,31,31,30,31,30,31]
month_of_last_year = [31,28,31,30,25]
## THIS CODE CACULATE THE DECLINATION ANGLE FOR
## THE NORMAL YEAR, LEAP YEAR, AND THE LAST YEAR
for i in month_day:
    b += i
    sn = 23.45*math.sin(math.radians((360/365)*(284 + b)))
    snn.append(sn)
b = 0
print('snn',snn)
for i in month_leap_day:
    b += i
    sn = 23.45*math.sin(math.radians((360/365)*(284 + b)))
    snn_leap_year.append(sn)
print('snn_leap_year',snn_leap_year)
b = 0
for i in month_of_last_year:
    b += i
    sn = 23.45*math.sin(math.radians((360/365)*(284 + b)))
    snn_last_year.append(sn)
print('sun_last_year',snn_last_year)
# ## algorithm for sunset hour angle
##THIS COMPUTES THE SUNSET ANGLE FOR
## EVERY YEAR
ws_normal= []
ws_leap= []
ws_last_year= []
l = 6.86 * (math.pi/180)
for sn in snn:
    ws_normal.append(math.degrees(math.acos(-math.tan(math.radians(l))*math.tan(math.radians(sn)))))
print('ws_normal', ws_normal)
for sn in snn_leap_year:
    ws_leap.append(math.degrees(math.acos(-math.tan(math.radians(l))*math.tan(math.radians(sn)))))
for sn in snn_last_year:
    ws_last_year.append(math.degrees(math.acos(-math.tan(math.radians(l))*math.tan(math.radians(sn)))))
# ## algorithm for the inverse relative distance of the earth sun
# ## where n is the number of years
month_day = [31,28,31,30,31,30,31,31,30,31,30,31]
dv_normal_year = []
dv_leap_year = []
dv_last_year = []
mk = 0
for i in month_day:
    mk = mk+i
    dv_normal_year.append(1 + 0.033*(math.cos(math.radians((360/365)*mk))))
mk = 0
for i in month_leap_day:
    mk = mk + i
    dv_leap_year.append(1 + 0.033*(math.cos(math.radians((360/365)*mk))))
mk = 0
for i in month_of_last_year:
    mk = mk + i
    dv_last_year.append(1 + 0.033*(math.cos(math.radians((360/365)*mk))))
### THESE LISTS HOLD THE EARTH RELATIVE INVERSE ANGLE
normal_years = [dv_normal_year,ws_normal,snn] #dv, ws, #sn
leap_years = [dv_leap_year,ws_leap,snn_leap_year]
last_years = [dv_last_year, ws_last_year,snn_last_year]
## ALGORITHM FOR EXTRA-TERRESTIAL ANGLE
mi = -1
Ra_normal = []
Ra_leap = []
Ra_last = []
const_q0 = 118.08
#+ 'MJ'/M2day
for i in zip(dv_normal_year, ws_normal, snn):
    z = (const_q0*i[0])/math.pi
    x = math.cos(math.radians(l))*math.cos(math.radians(i[2]))*math.sin(math.radians(i[1]))
    y = (math.pi/180)*i[1]*math.sin(math.radians(l))*math.sin(math.radians(i[2]))
    Ra_normal.append(z*(x+y))
print('Ra_normal',Ra_normal)
for i in zip(dv_leap_year,ws_leap,snn_leap_year):
    z = (const_q0 * i[0]) / math.pi
    x = math.cos(math.radians(l)) * math.cos(math.radians(i[2])) * math.sin(math.radians(i[1]))
    y = (math.pi / 180) * i[1] * math.sin(math.radians(l)) * math.sin(math.radians(i[2]))
    Ra_leap.append(z * (x + y))
print('Ra_leap',Ra_leap)
for i in zip(dv_last_year,ws_last_year,snn_last_year):
    z = (const_q0 * i[0]) / math.pi
    x = math.cos(math.radians(l)) * math.cos(math.radians(i[2])) * math.sin(math.radians(i[1]))
    y = (math.pi / 180) * i[1] * math.sin(math.radians(l)) * math.sin(math.radians(i[2]))
    Ra_last.append(z * (x + y))
print('Ra_last',Ra_last)
## Rs where Krs is the adjusted coefficient
Krs = 0.16
Rs_2015 = []
Rs_2016 = []
Rs_2017 = []
Rs_2018 = []
Rs_2019 = []
### ALGORITHM MONTHLY AVERAGE GLOBAL SOLAR RADIATION
for i in zip(maximum_temperature1_total[0],min_temp1_total[0],Ra_normal):
    Rs_2015.append(Krs*(math.sqrt(i[0]-i[1]))*i[2])
print('Rs_2015',Rs_2015)
for i in zip(maximum_temperature1_total[1],min_temp1_total[1],Ra_leap):
    Rs_2016.append(Krs*(math.sqrt(i[0]-i[1]))*i[2])
print('Rs_2016',Rs_2016)
for i in zip(maximum_temperature1_total[2],min_temp1_total[2],Ra_normal):
    Rs_2017.append(Krs*(math.sqrt(i[0]-i[1]))*i[2])
print('Rs_2017',Rs_2017)
for i in zip(maximum_temperature1_total[3],min_temp1_total[3],Ra_normal):
    Rs_2018.append(Krs*(math.sqrt(i[0]-i[1]))*i[2])
print('Rs_2018',Rs_2018)
for i in zip(maximum_temperature1_total[4],min_temp1_total[4],Ra_last):
    Rs_2019.append(Krs*(math.sqrt(i[0]-i[1]))*i[2])
print('Rs_2019',Rs_2019)

## NESTING THE LIST INTO A LIST FOR EASY
## DATA QUERY
data_unified_2015 = [maximum_temperature1_total[0],min_temp1_total[0],Ra_normal,Rs_2015]
data_unified_2016 = [maximum_temperature1_total[1],min_temp1_total[1],Ra_leap,Rs_2016]
data_unified_2017 = [maximum_temperature1_total[2],min_temp1_total[2],Ra_normal,Rs_2017]
data_unified_2018 = [maximum_temperature1_total[3],min_temp1_total[3],Ra_normal,Rs_2018]
data_unified_2019 = [maximum_temperature1_total[4],min_temp1_total[4],Ra_last,Rs_2019]
gd = 0
finished_2015 = []
finished_2016 = []
finished_2017 = []
finished_2018 = []
finished_2019 = []
## THIS FOR LOOP UNIFIES THE MAX_TEMP, MIN_TEMP
## EXTRA-TERRESTIAL ANGLE AND AVERAGE GLOBAL SOLAR
## RADIATION
for mb in range(12):
    for i in data_unified_2015:
        finished_2015.append(i[mb])
for mb in range(12):
    for i in data_unified_2016:
        finished_2016.append(i[mb])
for mb in range(12):
    for i in data_unified_2017:
        finished_2017.append(i[mb])
for mb in range(12):
    for i in data_unified_2018:
        finished_2018.append(i[mb])
for mb in range(3):
    for i in data_unified_2019:
        finished_2019.append(i[mb])
dc = 0
dd = -1
finished_2015_done = []
finished_2016_done = []
finished_2017_done = []
finished_2018_done = []
finished_2019_done = []
for i in finished_2015:
    dc += 1 ## this variable works with modulus method
    #  to ensures that a new folder is added after every forth count
    # of the loop
    if dc % 4 ==1:
        dd += 1## this is an index variable that starts from 0 and ends at 12
        ## it only increases  at every multiple of 4, following the modulus
        ## method
        finished_2015_done.append([])
    if len(finished_2015_done[dd]) <= 4:## this ensures that each list hold
        ## only 4 items
        finished_2015_done[dd].append(i)
dc = 0
dd = -1
for i in finished_2016:
    dc += 1
    if dc % 4 ==1:
        dd += 1
        finished_2016_done.append([])
    if len(finished_2016_done[dd]) <= 4:
        finished_2016_done[dd].append(i)
dc = 0
dd = -1
for i in finished_2017:
    dc += 1
    if dc % 4 ==1:
        dd += 1
        finished_2017_done.append([])
    if len(finished_2017_done[dd]) <= 4:
        finished_2017_done[dd].append(i)
dc = 0
dd = -1
for i in finished_2018:
    dc += 1
    if dc % 4 ==1:
        dd += 1
        finished_2018_done.append([])
    if len(finished_2018_done[dd]) <= 4:
        finished_2018_done[dd].append(i)
dc = 0
dd = -1
for i in finished_2019:
    dc += 1
    if dc % 4 ==1:
        dd += 1
        finished_2019_done.append([])
    if len(finished_2019_done[dd]) <= 4:
        finished_2019_done[dd].append(i)
## THIS LIST(finished_2015_don ) HOLDS UP THE LIST
## IN A SINGLE LIST SO THAT THEY CAN BE OPENED IN AN
## IN CSV FORMAT
finished_2015_don =[]
finished_2015_don.append(finished_2015_done)
with open('data_2015.csv','+w',newline='') as file:
    writingq = csv.writer(file,delimiter = ',')
    for rows in finished_2015_don:
        writingq.writerows(rows)
file.close()
finished_2016_don =[]
finished_2016_don.append(finished_2016_done)
with open('data_2016.csv','+w',newline='') as file:
    writingq = csv.writer(file,delimiter = ',', dialect= csv.excel)
    for rows in finished_2016_don:
        writingq.writerows(rows)
file.close()
finished_2017_don =[]
finished_2017_don.append(finished_2017_done)
with open('data_2017.csv','+w',newline='') as file:
    writingq = csv.writer(file,delimiter = ',', dialect= csv.excel)
    for rows in finished_2017_don:
        writingq.writerows(rows)
file.close()
finished_2018_don =[]
finished_2018_don.append(finished_2018_done)
with open('data_2018.csv','+w',newline='') as file:
    writingq = csv.writer(file,delimiter = ',', dialect= csv.excel)
    for rows in finished_2018_don:
        writingq.writerows(rows)
file.close()
finished_2019_don =[]
finished_2019_don.append(finished_2019_done)
with open('data_2019.csv','+w',newline='') as file:
    writingq = csv.writer(file,delimiter = ',',lineterminator = '\n', dialect= csv.excel)
    for rows in finished_2019_don:
        writingq.writerows(rows)
file.close()

## ploting data with matplotlib
mon_ax = [1,2,3,4,5,6,7,8,9,10,11,12]
# plt.plot(mon_ax,maximum_temperature1_total[0])
# plt.plot(mon_ax,min_temp1_total[0])
# plt.ylabel('Temperature')
# plt.xlabel('Month')
# plt.title('plot of maximum temperture, minimum temperature against month')
# plt.legend()

## histogram

plt.figure(figsize=(8,5))
plt.hist(x = (maximum_temperature1_total[0],min_temp1_total[0]),
         bins = range(12),label=['maximum temperature','minimum temperature'],align = 'left')
plt.legend()
plt.xlabel('months')
plt.ylabel('temperature')
plt.show()