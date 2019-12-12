# -*- coding: utf-8 -*-
"""
Created on Thu May 23 12:46:33 2019

@author: 15301093
"""

yr=int(input("Enter year: "))
if yr%4==0:
    if yr%100==0:
        if yr%400==0:
            print("Yes, it is a leap year.")
        else:
            print("No, it is not a leap year.")
    else:
         print("Yes, it is a leap year.")
else:
    print("No, it is not a leap year.")         