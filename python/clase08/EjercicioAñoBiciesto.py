'''
Diseñar un programa que ingresado un año, nos devuelva
por consola si es un año bisiesto o no, repetir la accion
gasta que el usuario lo desida.
'''

while opcion != "N":

    print("Comprobamos que año es bisiesto")
    anio = int(input("Ingrese el año:"))

    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")

     opcion = (input("Desea comprobar otro año) si/no: ")
               print("Fin del programa")
    