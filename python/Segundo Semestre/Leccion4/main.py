#Lista = Ariel, Liliana, Natalia, Osvaldo
#Colecciones en Python

#Las lista es lo que se conoce en tros lenguajes como arreglos o vectores

nombres =['Naty','Osvaldo','Lily','Ariel']
print(nombres)
print(nombres[0:2])#Solo muestra el indice 0, 1 pero no el 2
#Ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3])#Indices a mostrar 0,1,2
#Desde el indice indicado hasta el final
print(nombres[1: ])
#Modificamos un valor
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)

#Iterar una lista

for nombre in nombres: #nombre es singular, la ,lista es plural
    print(nombre)
else:
    print('Se acabaron los nombres de la lista')

#Preguntamos cuantos elementos tiene
print(len(nombres)) # le pasamos como parametro la lista

#Agregamos un elemento
nombres.append('Marcelo')
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append([7])
print(nombres)

#Insertar un elelemento en un indice especifico
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3,'Debora')
print(nombres)

#Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)

#Eliminar el último elemento
nombres.pop()
print(nombres)
#Eliminar un indice específico
del nombres[2] #del significa delete(eliminar)
print(nombres)

#Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

#Eliminar lista
del nombres
#print(nombres)

#Definimos una tupla
cocina =('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))

#Acceder a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[-1])

#Acceder a un rango
print(cocina[0:2])

#Ejemplo
verduras =('papa',)#Una tupla necesita aun que sea un elemento: la coma
#de lo contrario solo seria un tipo de str cadena

# Recordamos los elementos de la tupla
for cocinar in cocina:#Print esta usando diagonal inversa n para saltos de líneas
    print(cocinar, end= ' ') # Usamos end= para eliminar los saltos de líneas

cocinaLista = list(cocina)
cocinaLista[0] = 'plato'
cocina = tuple(cocinaLista)
print('\n',cocina)

#del cocina esto es para eliminar una tupla

#Tipos set
planetas = { 'martes', 'júpiter', 'venus'}
print(len(planetas)) # usamos la funcion len = lengnt significa largo

#Revisar si un lemento existe dentro del set
print('júpiter' not in planetas)

#Agregar un elemento
planetas.add('Tierra')# add es una funcion
print(planetas)

#Eliminar elementos , puede arrojar un error si el elemento no existe
planetas.remove('júpiter')#Esta funcion ante un mal ingreso u inexistenacia del elemento da error
print(planetas)
planetas.discard( 'Tierra')#Esta función no nos presenta ningún error
print(planetas)

#Limpiar set
planetas.clear()
print(planetas)

#Eliminar set o conjunto
del planetas
#print(planetas) #Al eliminar nos muestra fun error


#'Maradona' : 10 Un diccionario esta compuesto por dos elementos
#UNA LLAVE Y UN VALOR
#dict(key,valua)
diccionario = {
    'IDE':'Ingtegrated Development Enviorment',
    'POO':'Programación Orientada a Objetos',
    'SABD':'Sistema de Administración de Base de Datos'
}
#Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

#Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

#Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

#Modificar los elementos
diccionario['IDE']='Entorno de Desarrollo Integrado'
print(diccionario)

#Como recorrer los elementos
for termino in diccionario: #Recorremos mostrando solo las llaves
    print(termino)

#Necesitamos una función para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

#Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino) #Muestra solo las llaves

for valor in diccionario.values():#Usamos una funcion para acceder al valor
    print(valor)

#Comprobar la existencia de algun elemento
print('IDE' in diccionario) #Devuelve un booleano

# Agregar un elemento
diccionario['PK']= 'Primary Key'
print(diccionario)

#Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

#Vaciar un diccionario
diccionario.clear()
print(diccionario)

#Eliminar diccionario
del diccionario #El diccionario se borro

#Concatenar listas
listas1= [1, 2, 3, 1]
listas2 = [4, 5, 6, 1]
listas3 = listas1 + listas2#Concatenamos
print(listas3)

listas3.extend([7,8,9])#Funcionpara agregar varios elelmntos a una sola lista
print(listas3)

print(listas3.index(5))#Función para ubicar en que indice esta el valor a una lista
#print(listas3.count(0)) # esto daria un error por no ser el elemnto parte de la lista

#Como saber cuantos valores repetidos hay en una lista
print(listas3.count(1))

#Para poner al reves una lista
listas3.reverse()
print(listas3)

#Para que una lista se multiplique repitiendo sus elementos
listas3 = listas3 * 2
print(listas3)

#Metodo de ordenamiento

listas3.sort()#Ordena los elementos ascendentemente
print(listas3)
listas3.sort(reverse=True) # Ordena descendentemente
print(listas3)

tupla = (4, 'Hola', 6.78, [1,2,78], 4, 'Hola') #Puede identificar diferentes tipos de datos dentro
print(tupla)

print(4 in tupla) #Accion booleana, su respuesta es de tipo boolena
#Lo que podemos usar dentro de tuplas son: index, count,len
#En tuplas se puede convertir de tupla a listas y listas a tuplas

#Repaso de set o conjunto
#para definir un conjunto
conjunto= set()
conjunto1 = {}
conjunto.add(7)
conjunto.add('Hola')
print(conjunto)






























