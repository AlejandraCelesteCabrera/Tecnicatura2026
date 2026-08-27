'''
Ejercicio 04:Suponga que se tiene un conjunto de calificaciones de grupo 10 alumnos.
Realizar un algoritmo para calcular la calificacion promedio y la calificacion
más baja de tdo el grupo

'''

suma = 0
calificacionBaja = 9999
for i in range(1,11):
    calificacion = float(input(f"Ingrese la calificacion del alumno {i}: "))

    suma += calificacion

   if calificacion  < calificacionBaja:
       calificacionBaja = calificacion

 calificacionPromedio = calificacion / 10
print(f"La calificacion promedio es{calificacionPromedio}")
print(f"La calificacion más baja es :{calificacionBaja}")