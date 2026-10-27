from Persona import persona1


class Persona2:
    def __init__(self, nombre, apellido, edad):
         self._nombre = nombre
         self._apellido = apellido
         self._edad = edad

    def mostrar_detalle(self):
        print(f' los datos a mostar son los siguientes : {self._nombre} {self._apellido} {self._edad}')

    @property # decorador
    def nombre(self): # Metodo Getter
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):# metodo setter
        print('Estamos utilizando el método set')
        self._nombre = nombre

    @property
    def apellido(self, apellido):
        return self._apellido

    @apellido.setter
    def edad(self,apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self,edad):
       self._edad = edad

persona1 = Persona2('Ariel','Bentacud', 41)
print(persona1.nombre) #Llamamos al metodo getter
persona1.nombre = 'Juan Pedro' #Llamamos al metodo setter0
print(persona1.nombre)
print(persona1.mostrar_detalle())
# Atributo read-only seria la edad porque no tiene el método set
print(persona1.edad)
# Clase 7 parte 2 video 10.3 (por ver)