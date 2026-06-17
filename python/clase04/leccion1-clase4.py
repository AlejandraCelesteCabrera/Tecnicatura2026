'''
operandoA = 8
operandoB = 5

suma = operandoA + operandoB
print('Resultado de la suma:',suma)
print(f'El resultado de la suma es: {suma}')

resta = operandoA - operandoB
print(f'Resultado de la resta:,{resta}')

multiplicacion = operandoA * operandoB
print(f'Resultado de la multiplicacion es: {multiplicacion}')

division = operandoA / operandoB
print(f'Resultado de la division es: {division}')

division = operandoA // operandoB
print(f'Resultado de la division es: {division}')

Modulo = operandoA % operandoB
print(f'Resultado de la division o residuo (modulo) es: {Modulo}')

exponente = operandoA ** operandoB
print(f'Resultado del exponente es: {exponente}')
'''
'''
alto = int(input("Proporciona el alto del rectangulo: "))
ancho = int(input("Proporciona el ancho del rectangulo: "))
area = alto * ancho
perimetro = (alto + ancho) * 2
print('perimetro es: ', perimetro)
'''
'''
miVariable3 = 10
print(miVariable3)

#Operadores de reaccionacion
miVariable3 = miVariable3 +1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

#miVariable 3= miVariable - 2
miVariable3 -= 2
print(miVariable3)

#miVariable 3= miVariable * 2
miVariable3 *= 3
print(miVariable3)

#miVariable 3= miVariable / 2
miVariable3 /= 2
print(miVariable3)

#operadores de Comparacion

d = 4
b = 2
resultado = d == b #comprobamos si son iguales
print(resultado)

#Operador diferente
resultado = d != b
print(resultado)

#Operador Mayor que
resultado = d > b
print(resultado)

#Operador menor que
resultado = d < b
print(resultado)

#Operador menor o igual que
resultado = d <= b
print(resultado)

#Operador mayor o igual que
resultado = d >= b
print(resultado)
'''
'''
a = int(input("Digite un numero: "))
print(f'El residuo de la division es: {a % 2}')
if a % 2 == 0:
    print(f"El valor de a es: {a} es un numero PAR")
else:
    print(f"El valor de a es: {a}  es un numero IMPAR")
'''
'''
edadAdulto = 18
edadPersona = int(input(f' Digite su edad: '))
if edadPersona >= edadAdulto:
    print(f'La edad es {edadPersona} usted es mayor de edad')
else:
    print(f'La edad es {edadPersona} usted es menor de edad')
'''