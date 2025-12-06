# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 11:24:02 2025

@author: BEYZA NUR
"""

#task 21

def my_greeting_print(name):
    print(f"Hello {name}")


user_input = input("Please input an argument: ")
my_greeting_print(user_input)

#task 22
def my_greeting_return(name):
    return f"Hello {name}"


user_input = input("Please input an argument: ")
message = my_greeting_return(user_input)
print(message)

#task 23


def sum(num1, num2):
    return num1 + num2


print(sum(3, 2))

#task 27

password = input("Enter your password: ")
verification = ""
is_same = False

while not is_same:
    verification = input("Enter again: ")
    if verification == password:
        is_same = True
    else:
        print("They are not same.")

print("Your password matches and account created successfully")

#task 30

print("dumb calculator v0.1 If you want to exit, enter 0")

total_sum = 0
total_count = 0
odd_count = 0
even_count = 0
user_input = -1
while user_input != 0:
    user_input = int(input("please enter a number: "))
    
    if user_input != 0:
        total_sum += user_input
        total_count += 1
        
        if user_input % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

mean_value = 0
if total_count > 0:
    mean_value = total_sum / total_count
    
print(f"Total Number: {total_count}")
print(f"Sum: {total_sum}")

print(f"Mean: {mean_value}") 
print(f"Odd: {odd_count} Even: {even_count}")

#yapay zekadan yardım aldım.
