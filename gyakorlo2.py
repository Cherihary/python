#1

import random
x = 0
y = 0
for i in range(20):
    iranyok = ("Észak","Dél","Kelet","Nyugat")
    irany = random.choice(iranyok)
    if irany == "Észak":
        y += 1
    elif irany == "Dél":
        y -= 1
    elif irany == "Kelet":
        x += 1
    else:
        x -= 1
print(f"x,y: {x}, {y}")
print(f"Távolság: {abs(x) + abs(y)}")

#2

osszeg = 0
for nap in range(1,11):
    talalt_penz = random.randint(100,500)
    osszeg += talalt_penz
    print(f"{nap}. nap. Találtam {talalt_penz} Ft-ot. Összesen {osszeg} Ft")
    if osszeg > 2500:
        print("Vehetek egy pizzát.")
        osszeg -= 2500

#3

szokoz = 10
for szorzo in range(1,11):
    print(" "*szokoz, end="")
    print("*"*szorzo*2)
    szokoz -= 1

#4

a = 0; e = 0; i = 0; o = 0; u = 0
mondat = "Merry Christmas and Happy New Year"
for betu in mondat.lower():
    if betu == "a": a += 1
    elif betu == "e": e += 1
    elif betu == "i": i += 1
    elif betu == "o": o += 1
    elif betu == "u": u += 1
print(a, e, i, o, u)

#5

nojogsi = 0
for auto in range(1,16):
    sebesseg = random.randint(30,100)
    if sebesseg <= 50:
        print(f"{auto}. Szabályos")
    elif 51 <= sebesseg <= 60:
        print(f"{auto}. Gyorshajtás - Csekk: 20000 Ft")
    else:
        print(f"{auto}. Durva szabályszegés - Jogosítvány elvétele!")
        nojogsi += 1
print(f"{nojogsi} embernek vették el a jogosítványát.")

#6

talalt = False
for i in range(3):
    pin_kod = int(input("Add meg a PIN-kódod:"))
    if pin_kod == 1234:
        print("Belépés engedélyezve")
        talalt = True
        break
if talalt == False:
    print("Kártya zárolva")

#7

gyartosor = list()
for i in range(20):
    csoki = random.randint(90,110)
    gyartosor.append(csoki)
for csoki_suly in gyartosor:   #egyesével végigmegy a listaelemeken
    if  csoki_suly < 94 or csoki_suly > 106:
        print(f"{csoki_suly} SELEJT")
        selejt += 1
    else:
        print(f"{csoki_suly} OK")
print(f"Selejtek száma {selejt}")

#8

enpont = 0
szgpont = 0
for i in range(5):
    entipp = input("Kő, papír, olló?").lower()
    szgtipp = random.choice( ("kő","papír","olló") )
    if entipp == szgtipp:
        print("Mindkettőtök tippje a(z) {entipp}")
    elif entipp == "kő" and szgtipp == "olló" or \
        entipp == "olló" and szgtipp == "papír" or \
          entipp == "papír" and szgtipp == "kő":
        print("Megnyerted a kört")
        enpont += 1
    else:
        print("Elveszítetted a kört")
        szgpont += 1
if enpont > szgpont:
    print("Nyertél")
elif enpont < szgpont:
    print("Vesztettél")
else:
    print("Döntetlen")

#9

szoveg = input("Írj be egy mondatot:").lower()
for karakter in szoveg:
    if karakter == "a": ujszoveg += "4"
    elif karakter == "e": ujszoveg += "3"
    elif karakter == "i" or karakter == "í": ujszoveg += "1"
    elif karakter == "o": ujszoveg += "0"
    else: ujszoveg += karakter
print(ujszoveg.capitalize())

#10

prim = True
szam = int(input("Adj meg egy egész számot:"))
if szam < 0:
    print("A szám negatív, nem prím")
elif szam == 0:
    print("A szám nulla, nem prím")
elif szam == 1:
    print("A szám egy, nem prím")
elif szam == 2:
    print("A szám kettő, nem prím")
else:
    for oszto in range(2, szam // 2 + 1):
        if szam % oszto == 0:
            prim = False
            break
if prim:
    print(f"A {szam} prím")
else:
    print(f"A {szam} nem prím")

#11

szamlalo = 0
for perc in range(1,13):
    pulzus = random.randint(110,190)
    if pulzus < 140:
        zona = "Bemelegítő zóna"
    elif 140 <= pulzus <= 165:
        zona = "Zsírégető zóna"
    else:
        szamlalo += 1
        zona = "Anaerob zóna"
    print(f"{perc}. perc: {pulzus} bpm - {zona}")
print(f"Veszélyes zónába léptél {szamlalo} alkalommal")

#12

sarkanyhp = 300
for kor in range(1,6):
    print(f"{kor} kör")
    alapsebzes = random.randint(20,100)
    csapas = random.randint(1,5)
    if csapas == 5:
        alapsebzes*=2
        print("Kritikus csapás")
    elif csapas == 1:
        alapsebzes = 0
        print("Melléütött")
    else:
        print(f"Ennyivel sebezted a sárkányt:{alapsebzes}")
    sarkanyhp -= alapsebzes
    if sarkanyhp < 0:
        print("Győzelem")
        break

