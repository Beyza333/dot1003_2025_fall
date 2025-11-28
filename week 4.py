# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 11:28:26 2025

@author: BEYZA NUR
"""
#task 41

def longer_word(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    
    if len1 > len2:
        return word1
    elif len2 > len1:
        return word2
    else:
        return "Their length are same"


word1 = input("First Word: ")
word2 = input("Second Word: ")
print(longer_word(word1, word2))


word1_ex2 = input("First Word: ")
word2_ex2 = input("Second Word: ")
print(longer_word(word1_ex2, word2_ex2))


#task 42

user_input = input("Your Input: ")
print(f"*{user_input}*")

#task 51

sentence = "The quick brown fox jumps over the lazy dog"
search_input = ""

[cite_start]while search_input != "-1":
    search_input = input("What are you looking for? ")

    if search_input == "-1":
        [cite_start]print("Bye.") 
    else:
        [cite_start]index = sentence.find(search_input)

        if index != -1:
            [cite_start]print(f"found it at {index}") 
        else:
            [cite_start]print("not found") 
            
#yapay zekadan yarsım aldım.