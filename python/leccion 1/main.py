'''
miVariable = 3
print(miVariable)
miVariable = ("Hola a todos los estudiantes de la tecnucatura")
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))
#Las literales se escriben x240, la variable y =x984, la variable z = x304
print(id(y))
print(id(z))


# Tipes Int, float, String, Bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x ="Hola alumnos"
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de cadenas
miGrupofavorito = "ImagineDreagons"
caracteristicas = "The best pop band"
print("miGrupofavorito:", miGrupofavorito, caracteristicas)

numero1 = '7'
numero2 = '8'
print(int (numero1 )+ int(numero2))

#Tipos booleanos (bool)
miBooleano = 3 > 2
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

#Procesar la entrada del usuario
#Función imput
resultado = input("Digite un numero: ") #Ingresa un dato de tipo = stiring
#print(resultado)

#Conversion de la entrada de datos
numero1 = int(input("Escribir el primer numero: "))
numero2 = int(input("Escribir el segundo numero: "))
resultado = numero1 + numero2
print("el resultado es: ",resultado)
'''
from unittest import result

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
'''
#Operadores logicos

a= True
b= False
Resultado = a and b
print(Resultado)

#Operador OR
resultado = a and b
print(resultado)

#Operador not
resultado = a or b
print(resultado)
'''
'''
#Ejercicio :valor dentro de un rango
valor = int(input("Digite un numero: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = valor >= valorMinimo and valor <= valorMaximo
if dentroRango:
      print(f'El valor es {valor} esta dentro del rango')
else:
    print(f'El valor es {valor} No esta dentro del rango')
  '''
'''
#Ejercicio con el operador OR, Operador NOT

vacaciones = False
diaDescanso = True
if not (vacaciones or diaDescanso):
    print('Puede asistir al juego')
else:
    print('Tiene trabajo que hacer')
'''
''''
#Ejercicio: Rango entre 20 y 30 años
edad = int(input("Digite un numero: "))
veinte = edad >= 20 and edad <= 30
print(veinte)
treinta = edad >= 30 and edad <= 40
print(treinta)
'''
'''
#Sintaxis simplificada del operador
#If veinte or treinta
if (20 <= edad < 30) or (30 <= edad < 40):
    print("Estas dentro del rango de los (20'0) a (30'0) años")
#if veinte or treinta:
#   if veinte:
#      print('Estas dentro del rango de los (20 \'0) años')
#  elif treinta:
#     print('Estas dentro del rango (30\'0) años')
#    else:
#        print('No estas dentro del rango')
else:
    print("No estas dentro del rango de los (20\'0) a (30\'0) años")
'''
'''
#Ejercicio. El mator de dos numeros
numero1 = int(input("Digite el valor para el numero1"))
numero2 = int(input("Digite el valor para el numero2"))

if numero1 > numero2:
    print("El numero 1 es mayor")
else:
    print("El numero 2 es mayor")

'''

'''
#Ejercicio. Tienda de libro

print('Digite elos siguientes datos del libro')
nombre = input("Digite el nombre del libro: ")
id= int(input("Digite el id del libro: "))
precio= float(input("Digite el precio del libro: "))
envioGratuito = input("indicar si el loibro es gratuito (True / False): ")
if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    envioGratuito = 'El valor es incorrecto, debe escribir True/False'
print(f
        Nombre: {nombre}
        Id: {id}
        precio: {precio}
        envioGratuito: {envioGratuito}
'''















