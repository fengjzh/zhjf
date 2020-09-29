#coding:utf-8
'''
'Py'  --> 'pY'
'''

def convert(s):
    lst = [i.upper() if i.islower() else i.lower() for i in s]
    return "".join(lst)

s = 'Hello'
c = convert(s)
print(c)
