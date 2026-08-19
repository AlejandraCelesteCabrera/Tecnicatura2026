#Lista = Ariel, Liliana, Natalia, Osvaldo

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
