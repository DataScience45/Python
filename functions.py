#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 16:21:50 2020

@author: nareshlakkam
"""
"""
a = 10
b = 20
c = a+b
print(a,b,c)

x = "hello"
y = "hi"
z = x+y
print(x,y,z)

l = 12.34
m = 23.45
n = l+m
print(l,m,n)
"""

"""
#function    : summation
#description : adds two input arguments(digits, strings)
#return      : sum value 
"""
def user_sum(a,b):
    if(type(a) == str and type(b) != str):
        b = str(b)
    if(type(a) != str and type(b) == str):
        a = str(a)
    
    c = a + b
    print("arg1:{} arg2:{} sum={}".format(a,b,c))
    return c

c = user_sum(2,3)
c = user_sum("abc ","xyz ")
c = user_sum("abc ",1)
c = user_sum("abc ",12.34)
c = user_sum(12.34, "abc")

#keyword - for changeing the order
c = user_sum(b=1,a=2)

"""
#function    : summation with default parameter
#description : adds two input arguments(digits, strings)
#return      : sum value 
"""
def user_sum_default(a,b=5):
    if(type(a) == str and type(b) != str):
        b = str(b)
    if(type(a) != str and type(b) == str):
        a = str(a)
    
    c = a + b
    print("arg1:{} arg2:{} sum={}".format(a,b,c))
    return c

c = user_sum_default(2)
c = user_sum_default(2,10)
c = user_sum_default("abc")


"""
#function    : sum
#description : performs add,sub,mux and dev
#return      : add,sub,mux and dev values
"""
def calculator(a,b):
    u_add = 0
    u_sub = 0
    u_mux = 0
    u_dev = 0
    
    if(type(a) == int and type(b) == int):
        u_add = a + b
        u_sub = a - b
        u_mux = a * b
        u_dev = a/b if b != 0 else 0.1
    else:
        #one or more arguments are not digits
        print("invalid arguments")

    print("arg1:{} arg2:{} add={} sub={} mux={} dev={}".format(a,b,u_add, u_sub, u_mux, u_dev))
    return(u_add, u_sub, u_mux, u_dev)
    
u_a, u_s, u_m, u_d = calculator(10,0)


"""
#function    : var_sum
#description : adds multiple input arguments(only digits)
#return      : sum value 
"""
def var_sum(*args):
    totalArg = 0;
    for i in args:
        totalArg += 1
        print(i)
    c = sum(args)
    print("total arg={} sum = {}".format(totalArg, c))
    return c

var_sum(10,20)
var_sum(1,2,10,20,100,200,1000,2000)
var_sum(1,2,2.3,4.5,6.7)


"""
#function    : var_key
#description : adds multiple input arguments(only digits)
#return      : sum value 
"""
def var_key(**kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
# Driver code 
var_key(first ='Geeks', mid ='for', last='Geeks') 
var_key(mid ='for' ,last='Geeks',first ='Geeks') 