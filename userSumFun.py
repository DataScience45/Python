#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:44:29 2020

@author: nareshlakkam
"""


def user_sum_default(a,b=5):
    if(type(a) == str and type(b) != str):
        b = str(b)
    if(type(a) != str and type(b) == str):
        a = str(a)
    
    c = a + b
    print("arg1:{} arg2:{} sum={}".format(a,b,c))
    return c