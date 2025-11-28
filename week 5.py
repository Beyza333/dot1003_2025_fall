# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 11:33:31 2025

@author: BEYZA NUR
"""

#task 53
def create_spruce(height, box_size):
    
    max_spruce_width = 2 * height - 1

    
    if max_spruce_width > box_size:
        print("Hata: Kutu boyutu (Box Size) çam ağacının maksimum genişliğinden daha küçük.")
        print(f"Gereken minimum genişlik: {max_spruce_width}")
        return

   
    for i in range(1, height + 1):
       
        stars = 2 * i - 1
        
       
        leading_spaces = (box_size - stars) // 2 
        
       
        print(" " * leading_spaces + "*" * stars)

    
    trunk_width = 1
    
    
    trunk_spaces = (box_size - trunk_width) // 2
    
    
    print(" " * trunk_spaces + "*" * trunk_width)

# Ana Kod Başlangıcı
try:
   
    spruce_height = int(input("Çam ağacı yüksekliğini (Spruce height) girin: "))
    box_size = int(input("Kutu genişliğini (Box Size) girin: "))
    
    
    print("\n") 
    for _ in range(1):
        print(" " * box_size)


    create_spruce(spruce_height, box_size)

    
    for _ in range(3):
        print(" " * box_size)

except ValueError:
    print("Hata: Lütfen geçerli bir tam sayı girin.")
    
#task 58

def anarya(input_list):
    new_list = []
   
    for i in range(len(input_list) - 1, -1, -1):
        new_list.append(input_list[i])
    return new_list


game_list = []
user_input = ""

while user_input.lower() != "exit":
   
    
    if len(game_list) == 0:
        game_list.append("Doom")
        game_list.append("Max Payne")
        game_list.append("FTL")
        user_input = "exit" 
    else:
        user_input = input("Please enter a game name (or 'exit'): ")
        if user_input.lower() != "exit":
            game_list.append(user_input)

print(game_list)
print(anarya(game_list))



