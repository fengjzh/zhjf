#coding: utf-8

'''
password
'''

letter = input("Please input an English letter: ")
n = 3
pwd = ord(letter) + n
pwd_letter =  chr(pwd)
print(letter,"==>",pwd_letter)
