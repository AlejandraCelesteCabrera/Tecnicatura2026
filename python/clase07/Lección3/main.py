#Ciclo While (mientras o durante)
'''
contador = 0
while contador < 9:
    print('Ejecutando ciclo while',contador)
    contador += 1
else:
    print('Fin del ciclo')
'''
'''
#Imprimir números del 0 al 5 con el ciclo while
maximo = 5
contador = 0
while contador <= maximo:
    print(contador)
    contador += 1
'''

"""minimo = 1
contador = 5
while contador >= minimo:
    print(contador)
    contador -= 1"""
'''
#Ciclo For

cadena ='hello'
for letra in cadena:
    print(letra)
else:
    print('Fin del ciclo for')
 '''
"""#Palabra reservada break
for letra in 'Alemania':
    if letra == 'a':
        print(f'letra {letra}')
        break
else:
    print('Fin del ciclo for')"""

#Palabra Continue
for i in range(6):
    if i % 2 == 0:
        print(f'Valor {i}')

for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor {i}')