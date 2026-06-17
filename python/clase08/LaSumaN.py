'''
Calcular la suma de N primeros números
'''

N = int(input("Ingrese su numero: "))
suma = 0

for i in range(1,N + 1):
    suma = suma + i
print("La suma es: ",suma)