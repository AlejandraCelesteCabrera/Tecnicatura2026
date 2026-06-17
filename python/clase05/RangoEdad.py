'''
Ejercicio. Rango de Edad
'''

edad = int(input('Digite el numero de edad: '))
veinte = edad >= 20 and edad < 30
print(veinte)
treinta = edad >= 30 and edad < 40
print(treinta)

if veinte or treinta:
    print("Estas dentro del rango de los 20 a 30 años")
else:
    print("No estas dentro del rango de los 20 a 30")
    