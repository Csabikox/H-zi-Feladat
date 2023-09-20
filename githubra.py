# Bekérsz a felhasználótól 5db egész számot. Első körben mindegyiket vizsgáljuk meg, hogy pozitív e vagy negatív. Az 5-t közül hány db
# nagyobb mint 20.

szam1 = int(input("Kérlek adj meg egy számot:"))
szam2 = int(input("Kérlek adj meg egy számot:"))
szam3 = int(input("Kérlek adj meg egy számot:"))
szam4 = int(input("Kérlek adj meg egy számot:"))
szam5 = int(input("Kérlek adj meg egy számot:"))


if szam1 > 0:
    print("A szám pozitív")
else:
    print("A szám negatív")