def not_hesapla(satir):

    satir = satir[:-1]

    liste = satir.split(",")

    isim = liste[0]

    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    son_not = not1*(3/10) + not2*(3/10) + not3*(4/10)

    if(son_not >= 90):
        harf = "AA"

    elif(son_not >= 85):
        harf = "BA"

    elif (son_not >= 80):
        harf = "BB"

    elif (son_not >= 75):
        harf = "CB"

    elif (son_not >= 70):
        harf = "CC"

    elif (son_not >= 65):
        harf = "DC"

    elif (son_not >= 60):
        harf = "DD"

    elif (son_not >= 55):
        harf = "FD"

    else:
        harf = "FF"

    return isim + " " + harf + " \n"


def donem_sonu(satir):

    liste = satir.split(" ")

    harf = liste[2]

    if (harf == "FF"):

        durum = "Kaldı"

    elif(harf == "FD" or harf == "DD"):

        durum = "Koşullu"

    else:

        durum = "Geçti"

    return durum


with open("dosya.txt","r",encoding = "utf-8")as file:

    eklenecekler_listesi = []

    for i in file:

        eklenecekler_listesi.append(not_hesapla(i))


with open("notlar.txt","w",encoding="utf-8") as file2:

        for i in eklenecekler_listesi:
            file2.write(i)


with open("notlar.txt","r",encoding="utf-8") as file2:
    kalan = []
    kosullu = []
    gecti = []

    for i in file2:

        i = i[:-1]

        if (donem_sonu(i) == "Geçti"):

            sonuc = i + donem_sonu(i) + "\n"
            gecti.append(sonuc)

        elif(donem_sonu(i) == "Kaldı"):

            sonuc = i + donem_sonu(i) + "\n"
            kalan.append(sonuc)

        else:

            sonuc = i  + donem_sonu(i) + "\n"
            kosullu.append(sonuc)

with open("kalan.txt","w",encoding="utf-8") as file3:

    for i in kalan:
        file3.write(i)

with open("gecti.txt","w",encoding="utf-8") as file4:

    for i in gecti:
        file4.write(i)

with open("kosullu.txt","w",encoding="utf-8") as file5:

    for i in kosullu:
        file5.write(i)





