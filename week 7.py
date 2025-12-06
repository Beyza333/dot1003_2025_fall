# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 10:57:21 2025

@author: BEYZA NUR
"""

#task 67
def coordinator(x, y):
    """
    İki tamsayıyı bir demet olarak döndürür.
    """
    return (x, y)


my_coordinates = coordinator(5, 6)
print(my_coordinates)

#task 68
def coordinator(x, y):
    return (x, y)

my_coordinates = {}


my_coordinates[coordinator(0, 0)] = "Home"
my_coordinates[coordinator(1, 1)] = "Work"
my_coordinates[coordinator(-1, -1)] = "School"


for k, v in my_coordinates.items():
    print(f"position: {k} name: {v}")

#task 71
my_set = set()
flag = True

while flag:
    element = input("Enter an element for set: ")
    if element == "exit":
        flag = False
    else:
        my_set.add(element)


for item in my_set:
    print(item)

#task 72
my_set = set()
flag = True

while flag:
    element = input("Enter an element for set: ")
    if element == "exit":
        flag = False
    elif element in my_set:
        print(f"{element} is already in our set.")
    else:
        my_set.add(element)


for item in my_set:
    print(item)

#☻task 76
def yas_hesapla():
    """
    Kullanıcıdan geçerli bir doğum yılını (tamsayı) ister ve yaşını hesaplayıp döndürür.
    Geçersiz girişleri (metin, gelecek yıl) ele alır.
    """
    mevcut_yil = 2024  # Yaş hesaplaması için mevcut yılı varsaydık
    dongu_devam = True
    
    while dongu_devam:
        try:
           
            dogum_yili_girdi = input("Doğum yılınız nedir? ")
            
            dogum_yili = int(dogum_yili_girdi)
            
            
            if dogum_yili > mevcut_yil:
                print("Doğum yılı gelecekte olamaz. Lütfen tekrar deneyin.")
                continue  
            
            
            yas = mevcut_yil - dogum_yili
            
            dongu_devam = False
            
            
            return yas
            
        except ValueError:
            
            print("Geçersiz giriş. Lütfen bir sayı girin.")
        except Exception as e:
            
            print(f"Beklenmeyen bir hata oluştu: {e}")


print(f"Siz {yas_hesapla()} yaşındasınız.")

