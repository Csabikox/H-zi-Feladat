# Gyakorló

"""

number = int(input("Kérlek adj meg egy számot:"))

if number > 50:
    print("A megadott szám értéke nagyobb, mint 50!")
else:
    print("A megadott szám értéke kisebb, mint 50!")
    
"""
    
# 1.feladat: Kérj be a felhasználótól egy egész számot és vizsgáljuk meg, hogy pozitív vagy negatív szövegesen.

"""

szam = int(input("Kérlek adj meg egy számot:"))

if szam > 0:
    print("Pozitív")
else:
    print("Negatív")

"""

# 2.feladat: Készítsük fel a felhasználót arra

"""

jegy = int(input("Kérlek add meg az érdemjegyed:"))

if jegy == 1:
    print("Elégtelen")
if jegy == 2:
    print("Elégséges")
if jegy == 3:
    print("Közepes")
if jegy == 4:
    print("Jó")
if jegy == 5:
    print("Jeles")
if jegy > 5:
    print("Rossz adat")
if jegy < 1:
    print("Rosz adat")

"""


# Kulturált, leginteligensebb módszer:

"""
jegy = int(input("Kérlek add meg az érdemjegyed:"))

if jegy == 1:
    print("Elégtelen")
elif jegy == 2:
    print("Elégséges")
elif jegy == 3:
    print("Közepes")
elif jegy == 4:
    print("Jó")
elif jegy == 5:
    print("Jeles")
else:
    print("Rossz adat")
    
"""

# Vizsgáljuk meg, hogy kosárlabda vagy nem kosárlabda.

"""

hobby = input("Mi a hobbid:")

if hobby != "kosárlabda":
    print(" A hobbid nem a kosárlabda")
else:
    print(" A hobbid a kosárlabda")

"""

# Bekérünk a felhasználtól egy számot és megvizsgáljuk, hogy osztható 3-mal vagy sem.

"""

szam = int(input("Kérlek egy számot:"))

if szam % 3 == 0:
    print("A szám osztható 3-mal!")
else:
    print("A szám nem osztható 3-mal!")

"""

# Jegyre: 1.feladat: Kérjünk be a felhasználótól egy egész számot és vizsgáljuk meg,
#hogy pozitív negatív szövegesen és azt is írjuk ki, hogy páros e vagy páratlan.

szam = int(input("Kérek egy számot:"))

if szam > 0:
    print("Pozitív")
else:
    print("Negatív")
    
if szam 














# 2.feladat: Bekérünk egy számot és az adott órát reprezentálja ("1-23 ig az érték " ha 12 délelőtt ha 10 delelőtt van ha 15 delutan ha ezen kivűl akkor rossz adatott írunk
    
    