# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 11:14:17 2025

@author: BEYZA NUR
"""

#task 1
hours_in_day = 24
days_in_week = 7
hours_in_week = hours_in_day * days_in_week
minutes_in_hour = 60
seconds_in_minute = 60

minutes_in_week = hours_in_week * minutes_in_hour
seconds_in_week = minutes_in_week * seconds_in_minute

print("Hours in a week:")
print(hours_in_week)
print("Minutes in a week:")
print(minutes_in_week)
print("Seconds in a week:")
print(seconds_in_week)

#task 2

name = input("What is your name? ")
email = input("What is your email address? ")
nickname = input("What is your nickname? ")

print("\n##Let's review your information##")
print(f"Your name: {name}")
print(f"Your email address: {email}")
print(f"Your nickname: {nickname}")
print(f"\n{name} | {email} | {nickname}")

#task 3

name = input("Name: ")
victim = input("Victim: ")

print(f"Thank you, {name}!")
print(f"But our {victim} is in another castle!")

#task 4

name = "Courier"
age = 34
city = "New Vegas"
print(f"Hi {name}, you are {age} years old. You live in {city}.")

#♦task 5
name = "Ozan Akyol"
age = 18
skill1 = "python"
level1 = "beginner"
skill2 = "2d art"
level2 = "beginner"
lower = 2000
upper = 3000

print(f"My name is {name}, I am {age} years old")
print("\nMy skills are\n")
print(f"- {skill1} ({level1})")
print(f"- {skill2} ({level2})")
print(f"\nMy salary expectation is {lower}-{upper} euros/month")

#task 7
weight_kg = int(input("Enter your weight: "))
height_cm = int(input("Enter your height: "))
height_m = height_cm / 100.0

bmi = weight_kg / (height_m ** 2)

print(f"\nYour BMI is {bmi}")
# task 8

game_name = input("Game name: ")
release_year = int(input("Which year was this game released? "))
[cite_start]current_year = 2024 
game_age = current_year - release_year

print(f"\n{game_name} is {game_age} years old.")


#yapay zekadan yardım aldım.
