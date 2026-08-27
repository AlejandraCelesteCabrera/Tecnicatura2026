'''
Leer 10 números e imprimir cuantos son positivos cuantos
negativos y cuantos neutros.
'''

conteo_positivos = 0
conteo_negativos = 0
conteo_neutros = 0

for i in range (1,11):
num = int(input(f"Digite un número {i}"))

if num > 0:
    conteo_positivos += 1
elif num < 0:
    conteo_negativos += 1
else:
    conteo_neutros += 1

print(f"La cantidad de positivos son: {conteo_positivos}")
print(f"La cantidad de negativos son {conteo_negativos}")
print(f"la cantidad de neutros son {conteo_neutros}")
