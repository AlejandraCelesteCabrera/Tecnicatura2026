'''
Ingresar N enteros, visibilizar la suma de los números pares de la
lista, cuantos npumeros pares existen y cuales es el rpomedio de los
numero impares

n_elementos = int(input("Ingrese la cantidad de números: "))

i = 1
suma_pares = 0
conteo_pares = 0
suma_impares = 0
conteo_impares = 0

while i < n_elementos:
    num = int(input(f"Ingrese el numero {i}: "))

 if num % 2 == 0:
        suma_pares += num
        conteo_pares += 1
 else:
        suma_impares += num
        conteo_impares += 1
    i + 1


if conteo_pares == 0:
        print("No se han ingresado números pares.")
else:
        print(f"La suma de los npumeros pares es: {suma_pares}")
        print(f"Cantidad de numeros pares que existen: {conteo_pares}")

 #Resultado de números impare2
 if conteo_impares == 0:
     print("No se han ingresado números impares" )
 else:
     promedio_impares = suma_impares / conteo_impares
     print(f"El promedio de impares es: {promedio_impares}")
'''