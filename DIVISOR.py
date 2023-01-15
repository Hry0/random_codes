# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

num1=int(input("enter first number:- "))
num2=int(input("enter second number:- "))
if num1>num2:
    print()
    print("dividing",num1,"by",num2,"we find:-")
    remainder=num1%num2
    if remainder==0:
        print(num1,"is divisible by ",num2)
    else:
        print( num1,"is not divisible by", num2)
else:
    print()
    print("dividing",num2,"by",num1,"we find:-")
    remainder=num2%num1
    if remainder==0:
        print(num2,"is divisible by",num1)
    else:
        print(num2,"is not divisible by",num1)
        

#bye bye