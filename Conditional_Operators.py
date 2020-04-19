# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 17:51:43 2020

@author: Ramesh
"""


"""
==
!
<
<=
>
>=
"""

#Compare two numbers

x = 10

y = 12

if x>y:
    print("x is greater than y")
else:
    print("x is lessthan y")

#Conditional operator #Ternary Operator
print("x is greater than y") if x>y else print("x is lessthan y")

a=2 if x>y else 1

if x%2==0:
    print("x is even number")  #If ---use tab 
else:
    print("x is odd number")

#Logical Operators  And / OR / not

'a' or False
'a' or True
True or 'a'
False or 'a'

'a' and False
'a' and True  # for And---last valid statement...will get the last value -True
True and 'a'
False and 'a'


#Bit wise operators
x=15 #1111
y=7 #0111

print(x&y) #Bitwise And   7
print(x|y)  #Bitwise oR  15
print(x^y)  #Bitwise Xor  8
print(x>>1) #Bitwise rightshift 0111  ->7
print(y<<1) #Bitwise 1110 -->14

x=7  # have to multply wth 8 (no direct options)  For left shift///it will multiply by 2^n
#  for right shift ..it will diide by 2^n

print(7<<1) # 1110   14
print(7<<2) # 11100   
print(7<<3) # 111000
print(7<<4) # 1110000






















