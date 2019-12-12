# -*- coding: utf-8 -*-
"""
Created on Thu May 23 13:47:28 2019

@author: 15301093
"""

num = []
sum=0
for n in range(10):
    num.append(int(input("Enter number:")))
num.sort()
for n in range(10):
    sum=sum+num[n]
print("Smallest number: "+str(num[0]))
print("Largest number: "+str(num[9]))
print("Average: "+str(sum/10))
print("a. Difference between average and smallest number: "+str((sum/10)-num[0]))
print("b. Difference between average and smallest number: "+str(num[9]-(sum/10)))