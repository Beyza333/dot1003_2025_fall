# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 16:25:51 2025

@author: BEYZA NUR
"""

#task 79
#Iterative factorial calculator
def factorial(n):
    if n<0:
        raise ValueError("no negative value")
        if n==0 or n==1:
            return 1
    k=1
    for i in range (2,n+1):
        k*=i
        return k
print(factorial(5))
  #yapay zekadan yardım aldım.  
    
    