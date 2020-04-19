#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 17:17:47 2020

@author: nareshlakkam
"""

b = 100

"""
#function    : display
#description : displays variable
#return      : sum value 
"""
def display():
    #global b
    b = 20
    print(b) 
    
"""
#function    : update
#description : adds 10 to the global variable
#return      : sum value 
"""
def update():
    global b
    b += 10

print(b)

display()
print(b)

update()
print(b)
