# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 11:20:12 2025

@author: BEYZA NUR
"""

#task 11

fahrenheit = float(input("Please type in a temperature (F): "))

celsius = (fahrenheit - 32) * (5 / 9)

print(f"{fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius")

if celsius < 0:
    print("Brr! It's cold in here!")

#task 12

hourly_wage = float(input("Hourly wage: "))
hours_worked = float(input("Hours worked: "))
day_of_week = input("Day of the week: ")


if day_of_week.lower() == "sunday":
    
    daily_wages = (hourly_wage * 2) * hours_worked
else:
    daily_wages = hourly_wage * hours_worked

print(f"Daily wages: {daily_wages} liras")

#task 13

age = int(input("How old are you? "))
maturity_age = 18

if age >= maturity_age:
   
    
    if age >= 44:
        [cite_start]print("You are too old for this sh*t") # Bonus condition [cite: 63]
    else:
        [cite_start]print("Here is Dark Souls. Lol") # Over 18 and under 44 [cite: 67]
else:
    [cite_start]print("You can't play Dark Souls") # Under 18 [cite: 65]

#task 18

number = int(input("Enter number: "))


if number % 3 == 0 and number % 5 == 0:
    [cite_start]print("FizzBuzz") # [cite: 165]
elif number % 3 == 0:
    [cite_start]print("Fizz") # [cite: 157, 163]
elif number % 5 == 0:
    [cite_start]print("Buzz") # [cite: 159]

#task 19

number = int(input("Please type in a number: "))



if number > 0 and number % 2 == 0:
    print("The number is even")
elif number > 0 and number % 2 != 0:
    print("The number is odd")
else: # number <= 0
    print("The number is negative or zero")

#Yapay zekadan yardım aldım.