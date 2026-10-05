class Persona:

   def __init__(self, nombre, apellido, edad): #Se lo llama metodo Init Dunder
       self.nombre = nombre
       self.apellido = apellido
       self.edad = edad

   def mostrar_detalle(self):# self es iguala this
       print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


persona1 = Persona('Ariel', 'Bentacud', 40 )#Necesitamos enviar argumentos
print(persona1.nombre) #Tarea: hacer el print igual que co el objeto 2
print(persona1.apellido)
print(persona1.edad)

persona1 = Persona('Ariel', 'Bentacud', 40)
print(f'El objeto1 de la clase persona es: {persona1.nombre} {persona1.apellido} y su edad es: {persona1.edad}')

persona2 = Persona('Osvaldo', 'Giodadini', 45) #Necesitamos argumentos
print(f'El objeto2 de la clase persona : {persona2.nombre} {persona2.apellido}Su edad es: {persona2.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(f'El objeto1 modificado de la clase persona es: {persona1.nombre} {persona1.apellido} y su edad es: {persona1.edad}')


#Los atributos caracteristicas
#Los metodos son el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle()
persona2.mostrar_detalle()

Persona.mostrar_detalle()#Debemos pasarle una referencia para el self o dara error
persona1.telefono = '444455552'
print(persona1.telefono)
print(f'Este es el teléfono: {persona1.nombre} {persona1.telefono}')# Hemos creado un atributo de un objeto

# print(persona2.telefono) el objeto persona2 no tiene este atributo, da error
