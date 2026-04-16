def neliosumma(a, b):
    _tulos = a**2 + b**2
    return _tulos

#Pääohjelma
luku1 = float(input("Anna eka luku "))
luku2 = float(input("Anna toka luku: "))

#Tallennetaan funktion palauttama arvo globaaliin "tulos" muuttujaan, sitä voi käyttää uudelleen
tulos = neliosumma(luku1, luku2)
print("Laskun tulos on", tulos)

#Funktion palauttama arvo tulostetaan, mutta ei tallenneta, joten sitä ei voi käyttää uudelleen
print(neliosumma(tulos, luku1))

