#Operadores logicos
'''
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