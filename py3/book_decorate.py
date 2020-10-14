#-*- coding:utf-8 -*-
''''
File Name: book_decorate.py
Author: zhangjunfeng
Mail: 274788907@qq.com
Created Time: 2020-10-14 23:22:35
'''
def p_deco(func):
    def wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return wrapper
@p_deco
def book(name):
    return "the name of my book is {0}".format(name)

# zhjf = p_deco(book)
# py_book = zhjf("Python")

py_book = book("Python")

print(py_book)
