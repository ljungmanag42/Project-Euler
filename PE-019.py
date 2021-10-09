'''
Project Euler 19

You are given the following information, but you may prefer to do some 
research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century 
unless it is divisible by 400.  How many Sundays fell on the first of the 
month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

Answer = 

'''
import pandas as pd

monthDict = {
    'Jan':31,
    'Feb':28,
    'Mar':31,
    'Apr':30,
    'May':31,
    'Jun':30,
    'Jul':31,
    'Aug':31,
    'Sep':30,
    'Oct':31,
    'Nov':30,
    'Dec':31
    }
months = list(monthDict.keys())
weekdayDict = {
    1:'Sun',
    2:'Mon',
    3:'Tue',
    4:'Wed',
    5:'Thu',
    6:'Fri',
    7:'Sat'
    }

days = 1
weekday = 2
day = 1
month = 1 
year = 1900

counter = 0
while days<=36875:
    days+=1
    #print('%d-%0d-%0d' % (year,month,day))
    
    if day==1 and weekday==1 and year>=1901:
        counter+=1
    
    # Update date
    monthStr=months[month-1]
    dayMax=monthDict[monthStr]
    if year%4==0:
        if year%1000==0:
            if year%400==0:
                dayMax+=1
        else:    
            if monthStr=='Feb': 
                dayMax+=1    
        
    if weekday==7:
        weekday=1
    else:
        weekday+=1
        
    if day==dayMax:
        day=1
        if month==12:
            month=1
            year+=1
        else:
            month+=1
    else:
        day+=1
        
print('%d-%0d-%0d' % (year,month,day))
print('Number of Sundays on the 1st of the month: %d' % counter)





