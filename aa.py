#!/usr/bin/python
# -*- coding: UTF-8 -*-

year=int(raw_input("年：\n"))
month=int(raw_input("月：\n"))
day=int(raw_input("日：\n"))
months1=[0,31,60,91,121,152,182,213,244,274,305,335,366] #闰年
months2=[0,31,59,90,120,151,181,212,243,273,304,334,365] #平年

if ((year%4==0)and(year%100!=0)) or((year%100==0)and(year%400==0)):
    Dth=months1[month-1]+day
else:
    Dth=months2[month-1]+day
print "是该年的第%d天"%Dth