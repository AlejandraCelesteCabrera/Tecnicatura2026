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
show (*person) # Esto es lo mismo que lo anterior pero le pasamos todo junto
person2 = ('Osvaldo', 'Giodanini')# desempaqietamos a traves de una tupla
show(*person2)
persona3 = {'lastName': 'Lucero', 'name': 'Natalia'}
show(**persona3)

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
    if n == 3:
        break # Esta es la única manera para que no ejecute el else
else:
    print('Esto se terminó')


#List comprehension, lista de compresión
names = ['Paolo', 'Rodrigo', 'Lupe', 'Pepe']
alongP = [p for p in names if p[0] == 'P'] #Esto regresa una nueva lista
print(alongP)

bottleC =[{'name': 'Quilmes', 'Country': 'Arg'},
          {'name': 'Corona', 'Country': 'Mex'},
          {'name': 'Stella Artois', 'Country': 'Belgiun'}
         ]
Arg =[b for b in bottleC if b['Country'] == 'Arg']
print(Arg)
print(bottleC)

#Paso de argumentos (funciones)
def mi_funcion2(name, lastName):
    print('saludosa todos los que ven a través del canal de YpuTube')
    print(f'Nombre:{name}, Apellido:{lastName}')
mi_funcion2('Jorge', 'lucero')
mi_funcion2('Ariel', 'Betancud')
mi_funcion2('Analia', 'Pedrosa')

#Palabra return en funciones
#CREAMOS UNA FUNCIÓN PARA SUMAR
def sumar (a, b):
    return a + b
resultado = sumar(78, 22)
print(f'resultado de la suma es: {resultado}')
print(f'resultado de la suma es: {sumar(55,45)}')

def sumar2 (a = 0, b = 0)->int: #Le damos un valor or default
    return a + b
resultado = sumar2()
print(f'resultado de la suma es: {resultado}')
print(f'resultado de la suma es: {sumar(22,66)}')


#Argumentos, variables en funciones
def listaNombres(*nombres):#Normalmente se utiliza : +args
    for nombre in nombres:#Se va a convertir en una tupla
        print(nombre)
listaNombres('Lucas', 'Jose', 'Claudia', 'Rosa', 'Maria')
listaNombres('Marcos', 'Daniel', 'Romina', 'Pepe', 'Marcela', 'Carlos')

def listarTerminos(**terminos): #Los mas utilizado es **kwargs para recibir los argumentos
    for llave, valor in terminos.items(): #kwargs significa: key word argument
        print(f'{llave}: {valor}')

listarTerminos(IDE='Integrated Develoment Environment', PK='Primary Key')
listarTerminos(Nombre='lionel Messi')

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
#desplegarNombre(10,11) #No son objetos iterable
desplegarNombres((10, 11)) #La conveetimos a una tupla, en un solo elemento no olvidar la coma
desplegarNombres([(22,55)]) #La convertimos en una lista




