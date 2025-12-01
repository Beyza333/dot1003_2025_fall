# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 15:48:02 2025

@author: BEYZA NUR
"""
#task 77 (week 7)
x =int (input ("please enter a number:"))
flag =True
while flag :
    try:
          y=int (input("please enter divider:"))
          print(f"{x} divider by {y} is {x/y}")
          flag =False
    
        
    except ZeroDivisionError:
        print("you can't enter 0 as divider")
    except ValueError:
        print("invalid value")
    except :
        print("some kind of error occured")
        

    #yapay zekadan yardım aldım.
    
    

    
    
    
    