#-*- coding:utf-8 -*-
''''
File Name: gravity.py
Author: zhangjunfeng
Mail: 274788907@qq.com
Created Time: 2020-09-30 23:50:25
'''

def weight(g):
    def cal_mg(m):
        return m * g
    return cal_mg

w = weight(10)
G = w(100)
print(G)
