#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 17:24:08 2020

@author: nareshlakkam
"""

class MyClass:
    a=10
    b=20
    def displayA(self):
        print("a value is =%d" %(self.a))
    
    def displayB(self):
        print("b value is =%d" %(self.b))


c1 = MyClass()
c1.displayA()
c1.displayB()

c2 = MyClass()
c2.a = 200
c2.b = 300
c2.displayA()
c2.displayB()

#with constructor/init

class ConsClass:
    def __init__(self,arg_a,arg_b):
        self.a = arg_a
        self.b = arg_b
        print("init a=%d b=%d" %(self.a,self.b))
        
    def displayA(self):
        print("a value is =%d" %(self.a))
    
    def displayB(self):
        print("b value is =%d" %(self.b))

    def displayString(self,str1):
        print("string value is =%s" %(str1))

c2 = ConsClass(arg_a=200,arg_b=300)
c2.displayB()
c2.b = 400
c2.displayB()
c2.displayString("hi")


c3 = ConsClass(2,3)