#1

for szam in range(1,31):
    if szam % 2 == 0:
        print(f"{szam} páros")
    else:
        print(f"{szam} páratlan")

#2

for szam in range(100,201):
    if szam % 2 == 0:
        print(f"{szam} páros")
    else:
        print(f"{szam} páratlan")

#3

import random
veletlen = random.randint(1,20)
print(f"A véletlen szám {veletlen}")
print(f"Az osztói:")
for oszto in range(1,veletlen+1):
    if veletlen % oszto == 0:
        print(oszto, end=" ")

#4

harom = 0; ot = 0; egyikse = 0
for szam in range(1,51):
    if szam % 3 == 0:
        harom += 1
    if szam % 5 == 0:
        ot += 1
    if szam % 3 != 0 and szam % 5 != 0:
        egyikse += 1

print(f"\nHárommal osztható {harom}")
print(f"Öttel osztható {ot}")
print(f"Egyikkel se osztható {egyikse}")

#5
#2**2 négyzet

for szam in range(10,26):
    print(f"A szám: {szam}, négyzete {szam**2}, köbe {szam**3}")

#6

for csillagszam in range(1,11):
    print(csillagszam * "*")

#7

for szam in range(5,51):
    if szam < 10:
        print(f"{szam} egyjegyű")
    else:
        print(f"{szam} kétjegyű")

#8

for szam in range(50,9,-1):
    if szam % 7 == 0:
        print(f"Hetes szám")
    if szam % 2 == 0:
        print(f"Páros szám")
    if szam % 7 != 0 and szam % 2 != 0:
        print(szam)





