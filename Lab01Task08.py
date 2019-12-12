# -*- coding: utf-8 -*-
"""
Created on Thu May 23 13:39:09 2019

@author: 15301093
"""

num = []
print("Enter six numbers:")
for n in range(6):
    num.append(int(input("Enter number:")))
num.sort()
print("Sum of smallest and largest number: "+str((num[0]+num[5])/2))
print("Sum of second smallest and second largest number: "+str((num[1]+num[4])/2))
print("Sum of third smallest and third largest number: "+str((num[2]+num[3])/2))