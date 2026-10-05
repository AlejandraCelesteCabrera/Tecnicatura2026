#Ejercicio 01: Crear una función para sumar los valores recibidos de tipo
# numéricos, utilizando argumentos variables *args como parametro de la
#función y agregar como resultado la suma de todos los valores pasados
#como argumentos.
def sumar_valor(*args):  #recibimos una cantidad de parámetro indefinidos
    resultado = 0
    #Iteramos cada elemento
    for valor in args:
        resultado += valor
    return resultado


#Llamamos a la función
print(sumar_valor(3, 5, 9, 2, 1))
