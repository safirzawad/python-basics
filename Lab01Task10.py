# -*- coding: utf-8 -*-
"""
Created on Thu May 23 13:55:06 2019

@author: 15301093
"""

import math
print("Input the length of the three sides of the triangle:")
a=int(input("Enter length:"))
b=int(input("Enter length:"))
c=int(input("Enter length:"))
p=(a+b+c)/2
print("Area of the triangle: "+str(math.sqrt((p)*(p-a)*(p-b)*(p-c))))