# -*- coding: utf-8 -*-
"""
Created on Mon May 20 15:02:28 2019

@author: 15301093
"""
num=int(input("Enter number of copies to be printed: "))
if num<=100:
    print("Cost of print: "+str(num*50)+"won")
else:
    print("Cost of print: "+str((100*50)+((num-100)*35))+"won")