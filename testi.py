#Kysytään pituus ja paino
pituus = float(input("Kuinka pitkä olet? "))
paino = float(input("Paljonko painat? "))

#Tallennetaan bmi laskutoimituksen jälkeen muuttujaan
bmi = paino / (pituus / 100) **2

#Tulostetaan bmi
print("BMI:si on", bmi)
print(f"BMI:si on {bmi}.")