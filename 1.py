#-*- coding:utf-8 -*-
'''
File Name: 1.py
Author: zhangjunfeng
Mail: 274788907@qq.com
Created Time: 2020-11-27 16:19:23
'''
import sys

def test():
    print(sys.argv)
    args = len(sys.argv)
    if args == 1:
        print("Hello world!")
    elif args == 2:
        print('Hello %s!' % sys.argv[1])
    else:
        print("to many.")
if __name__ == '__main__':
    test()
