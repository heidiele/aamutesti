vuosi = int(input("Anna vuosiluku jonka haluat tarkistaa: "))

"""
if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi")
"""

#Toinen tapa
if vuosi % 4 == 0:
    if vuosi % 100 == 0:
        if vuosi % 400 == 0:
            print("On karkausvuosi.")
        else:
            print("ei ole karkausvuosi")
    else:
        print("on karkausvuosi")
else:
    print("ei ole karkausvuosi")