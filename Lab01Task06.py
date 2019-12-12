# -*- coding: utf-8 -*-
"""
Created on Thu May 23 13:05:11 2019

@author: 15301093
"""
sum=0
print("Printing average of all numbers divisible by 3 and less than 100:")
for num in range(1,100):
    if num%3==0:
        sum=sum+num
print(sum)