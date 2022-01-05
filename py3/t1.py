#!/usr/bin/env python3
'''
test
'''
def convert(s):
    for i in s:
        lst = [ i.upper() if i.islower() else i.lower() for i in s ]
        return "".join(lst)
