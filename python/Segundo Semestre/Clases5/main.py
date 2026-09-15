#Comenzamos funciones
# mi_funcion() #No se puede llamar antes de definir a un a funcion
#Definir una función
def mi_funcion(): #Para indetificar a la funcion utilizamos paréntesis
    print('Saludos a todos los alumnoos de la Tecnicatura')

mi_funcion() #Estamos llamando a la función
mi_funcion() # Se puede llamar a una función N cantidad de veces

#Desempaquetado de listas o list unpacking
def show (name, lastName):
    print(name+' '+lastName)
person = ["Ariel", "Betancud"]
show (person[0], person[1]) # pasamos uno por los datos de la lista de la función
show (*person) # Esto es lo mismo que lo anterior pero le pasamos todo