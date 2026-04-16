def summa(_a, _b):
    return print("Lukujen summa on:", a+b)

def erotus(_a, _b):
    return print("Lukujen erotus on:", a-b)

def tulo(_a, _b):
    return print("Lukujen tulo on:", a*b)

def jako(_a, _b):
    if _b != 0:
        print("Lukujen osamäärä on:", a / b)
    else:
        print("Nollalla ei voi jakaa!")
    return

print("\n------------------TERVETULOA KÄYTTÄMÄÄN LASKINTA!------------------")

while True:
    print("\nValitse mitä toimintoa haluat käyttää:\n A: Yhteenlasku \n B: Vähennyslasku \n C: Kertolasku"
          "\n D: Jakolasku")

    valinta = input("Valintasi (A-D, Q lopettaa): ").upper()

    if valinta == "Q":
        print("Ohjelma lopetetaan.")
        break

    a = float(input("Anna eka luku: "))
    b = float(input("Anna toka luku: "))

    if valinta == "A":
        summa(a, b)
    elif valinta == "B":
        erotus(a, b)
    elif valinta == "C":
        tulo(a, b)
    elif valinta == "D":
        jako(a, b)
    else:
        print("Virheellinen valinta tai luku.")

        