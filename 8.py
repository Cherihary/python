#1

import random
veletlen = random.randint(1,20)
for tipp in range(1,21):
    if tipp == veletlen:
        print(f"Tipp {tipp}: talált")
        break
    else:
        print(f"Tipp {tipp}: nem talált")

#2

osszeg = 0
ismetles = random.randint(10,20)
for i in range(ismetles):
    szam = random.randint(1,100)
    osszeg += szam
    print(f"A számok összege {osszeg}")
    print(f"A számok átlaga {osszeg/ismetles:.2f}")



