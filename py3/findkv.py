#-*- coding:utf-8 -*-
''''
File Name: findkv.py
Author: zhangjunfeng
Mail: 274788907@qq.com
Created Time: 2020-09-29 23:26:01
'''

def findkv(dct,**kwargs):
    r = {k:v for k,v in kwargs.items() if dct.get(k) == v}
    return r

d = {'a':39,'b':40,'c':99,'d':100}
fr = findkv(d,a=1,b=40)
print(fr)
