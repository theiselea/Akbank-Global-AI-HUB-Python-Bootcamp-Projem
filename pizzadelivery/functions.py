import csv
import main
boy=input("Seçmek istediğiniz boyu girin: ")

class Pizza():
        def get_description(self, isim, boy, fiyat):
            self.isim = isim
            self.boy = boy
            self.fiyat =fiyat

        def secim(self,secim):
            secim=input("Pizza boyunu seçiniz.Büyük-Orta-Küçük:")
            print("{} seçildi".format(secim))

        def boyut(self):
            print(' boyut seçildi')


class Cesit(Pizza):
    tutar = 0
    if main.base_choice == "Sade Pizza" or main.base_choice == "sade pizza" or  main.base_choice == "sade" or main.base_choice == "Sade":
        if boy == "Küçük":
            tutar = 65
        elif boy == "Orta":
            tutar = 75

        elif boy == "Büyük":
            tutar=85
        else:
            print("Yanlış ifade girdiniz!")

    elif main.base_choice == "Margarita Pizza" or main.base_choice == "margarita pizza" or  main.base_choice == "margarita" or main.base_choice == "Margarita":
        if boy == "Küçük":
            tutar = 70
        elif boy == "Orta":
            tutar = 80
        elif boy == "Büyük":
            tutar = 90
        else:
            print("Yanlış ifade girdiniz!")

    elif main.base_choice == "Klasik Pizza" or main.base_choice == "klasik pizza" or  main.base_choice == "klasik" or main.base_choice == "Klasik":
        if boy == "Küçük":
            tutar = 75
        elif boy == "Orta":
            tutar = 85
        elif boy == "Büyük":
            tutar = 95
        else:
            print("Yanlış ifade girdiniz!")

    elif main.base_choice == "Türk Pizza" or main.base_choice == "türk pizza" or  main.base_choice == "türk" or main.base_choice == "Türk":
        if boy == "Küçük":
            tutar = 75
        elif boy == "Orta":
            tutar = 85
        elif boy == "Büyük":
            tutar = 95
        else:
            print("Yanlış ifade girdiniz!")

    elif main.base_choice == "4 Peynirli Pizza" or main.base_choice == "4 peynirli pizza" or  main.base_choice == "4 peynirli" or main.base_choice == "4 Peynirli":
        if boy == "Küçük":
            tutar = 80
        elif boy == "Orta":
            tutar = 90
        elif boy == "Büyük":
            tutar = 100
        else:
            print("Yanlış ifade girdiniz!")

class Ek(Cesit):
    if main.sauce_choice == "Mısır":
        Cesit.tutar+=5
        print("Tutar= ", Cesit.tutar)
    elif  main.sauce_choice == "Zeytin":
        Cesit.tutar+=5
        print("Tutar= ", Cesit.tutar)
    elif main.sauce_choice == "Mantar":
        Cesit.tutar += 5
        print("Tutar= ", Cesit.tutar)
    elif main.sauce_choice == "Keçi Peyniri":
        Cesit.tutar += 5
        print("Tutar= ", Cesit.tutar)
    elif main.sauce_choice == "Füme Et":
        Cesit.tutar += 5
        print("Tutar= ", Cesit.tutar)
    elif main.sauce_choice == "Soğan":
        Cesit.tutar += 5
        print("Tutar= ", Cesit.tutar)
    elif main.sauce_choice == "Mısır":
        Cesit.tutar += 5
        print("Tutar= ", Cesit.tutar)
    else :
        print("Yanlış bir malzeme seçtiniz!")


name = input("Lütfen İsim ve Soyisim Girin: ")
tc = input("Lütfen TC Kimlik Numaranızı Girin: ")
kkno = input("Lütfen Kredi Kart Numaranızı Girin: ")
kkpw = input("Lütfen Kredi Kart Şifrenizi Girin: ")


with open("Orders_Database.csv","a") as info:
    write = csv.writer(info)
    write.writerow(input(name),input(tc),input(kkno),input(kkpw))
    write = csv.writer(main.base_choice,main.base_choice,main.sauce_choice,main.time)




