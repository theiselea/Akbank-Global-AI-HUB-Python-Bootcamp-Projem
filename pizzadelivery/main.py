import csv
import datetime
import os
import csv
import __main__

f = open("Menu.txt", "a")
f.write("""*Lütfen Bir Pizza Tabanı Seçin:
1.Klasik
2.Margarita
3.Türk Pizza
4.Sade Pizza
5.4 Peynirli Pizza
*Seçeceğiniz ürünler:
1.Zeytin 
2.Mantar
3.Keçi Peyniri
4.Füme Et
5.Soğan
6.Mısır
*Teşekkür ederiz!
""")
f = open("Menu.txt", "r")
print(f.read())

base_choice = (input("Lütfen Seçtiğiniz Tabanı Girin: "))
print("Seçtiğiniz taban {}. ".format(base_choice))
sauce_choice =(input("Lütfen Seçtiğiniz Ek Malzemeyi Girin: "))
print("Seçtiğiniz malzeme {}. ".format(sauce_choice))
time =  datetime.datetime.now()


