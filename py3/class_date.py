#-*- coding:utf-8 -*-
''''
File Name: class_date.py
Author: zhangjunfeng
Mail: 274788907@qq.com
Created Time: 2020-11-14 12:29:52
'''

class Date(object):
    def __init__(self,year=0,month=0,day=0):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls,date_as_string):
        year,month,day = map(int,date_as_string.split('-'))
        date1 = cls(year,month,day)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        year,month,day = map(int,date_as_string.split('-'))
        return day <=31 and month <=12 and day <= 2038

d = Date.from_string('2020-11-14')
is_date = Date.is_date_valid('2020-11-14')
print(is_date)
print(d.year)
