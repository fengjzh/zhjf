#!/usr/bin/python3.8

def convert(s):
    lst = [i.upper() if i.islower() else i.lower() for i in s]
    return "".join(lst)

def convert2(s):
    s1 = ""
    for i in s:
        if i.islower():
            i = i.upper()
        else:
            i = i.lower()
        s1 += i
    return s1

if __name__ == "__main__":
    s = 'Hello'
    c = convert(s)
    d = convert2(s)
    print(c)
    print(d)
