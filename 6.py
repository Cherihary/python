#1

import random
fejek = random.randint(1,9)
szinek= ("zöld","piros","fekete")
szin = random.choice(szinek)
if fejek == 1 and szin == "zöld":
    print("Szia Süsü.")
elif fejek in (1,2,3,4):
    print(f"A {szin} sárkány gyenge")
elif fejek in (5,6,7):
    print(f"A {szin} sárkány közepes erejű")
else:
    print(f"A {szin} sárkány félelmetes")

#2

kincsek = ("arany","ezüst","semmi")
kincs = random.choice(kincsek)
kulcs = random.randint(1,5)
if kulcs < 3:
    print("A kulcs túl gyenge, a láda zárva maradt")
elif kincs == "semmi":
    print("A láda üres")
else:
    print(f"A láda tartalma {kincs}")

#3

karakterek = ("lovag","kereskedő","paraszt")
karakter = random.choice(karakterek)
hid = random.randint(50,200)
suly = random.randint(70,120)
if hid < suly:
    print("A híd leszakadt, nem tudsz úszni és megfulladsz")
elif hid >= suly and (hid-suly) <= 10:
    print(f"A híd kissé recseg, de a {karakter} átér")
else:
    print(f"A {karakter} gond nélkül átjut a hídon")

#4

meseszamok = (3,7,9,12)
meseszam = random.choice(meseszamok)
jutalmak = ("drágakő", "arany", "ezüst")
jutalom = random.choice(jutalmak)
if meseszam % 2 == 0:
    print(f"Stb, a jutalmad {jutalom}")
elif meseszam in (3,9):
    print(f"Kisebb próba vár rád, de {jutalom} a jutalom")
else:
    print(f"Hét próbán kell keresztülmenned az életedért")

#5

specialitasok = ("tűz","víz","föld")
varazslo1 = random.choice(specialitasok)
varazslo2 = random.choice(specialitasok)
if varazslo1 == "tűz" and varazslo2 == "föld" or varazslo1 == "víz" and varazslo2 == "tűz" \
    or varazslo1 == "föld" and varazslo2 == "víz":
    print("Az első varázsló győzött")
elif varazslo1 == varazslo2:
    print("A varázslók nem bírtak egymással")
else:
    print("A második varázsló győzött")

#6


