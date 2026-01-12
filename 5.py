print("Hajrá fradi!")
#1

import random
kocka1 = random.randint(1,6)
lehetosegek = (1,2,3,4,5,6)
kocka2 = random.choice(lehetosegek)
print(f"Az első kocka értéke {kocka1}")
print(f"Az második kocka értéke {kocka2}")
if (kocka1 + kocka2) % 2 == 0:
    print("Páros a dobás eredménye")
else:
    print("Páratlan a dobás eredménye")

#2

tipp = input("Fej vagy írás?").lower()
# fej, írás, Fej, Írás, FEJ, ÍRÁS
oldalak = ("fej","írás")
erme = random.choice(oldalak)
if tipp == erme:
    print("Nyertél")
else:
    print("Vesztettél")

#3

jegy = random.randint(1,5)
szoveges = ("elégtelen", "elégséges", "közepes", "jó", "jeles")
print(f"Az osztályzatod {jegy} ({szoveges[jegy-1]})")

#5

meseszam = random.randint(1,10)
if meseszam in (3,7,9):
    print(f"A véletlen egy meseszámot sodort eléd")
else:
    print(f"A mesék a gyerekeknek valók")

#6

allatok = ("kutya","macska","ló","tehén")
valasztas = random.choice(allatok)
if valasztas == "kutya" or valasztas == "macska":
    print(f"A {valasztas} háziállat")

#7

szam = random.randint(1,100)







