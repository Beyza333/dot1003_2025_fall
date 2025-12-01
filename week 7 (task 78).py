# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 16:25:34 2025

@author: BEYZA NUR
"""

#task 78
game_list=[]
def new_game():
    flag=True
    while flag:
        user_command =input ("add or exit:")
    if user_command =="exit":
            flag =False
    elif user_command=="add":
            game_list.append(new_game())
    for game in game_list:
        print(f" Name:{game[0]}, Year:{game[1]}")
        
    #yapay zekadan yardım aldım.
        


    


        
       
