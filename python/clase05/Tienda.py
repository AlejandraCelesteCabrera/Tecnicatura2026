'''
Ejercicio: Tienda de los libros
mostrar: Imgrese los siguientes datos del libro
Digite el nombre del libro
Digite el ID del libro
Indicar si el envio es gratuito
'''


print("Digite el nombre del libro")
nombre = input("Digite el nombre del libro: ")
id = int(input("Digite el ID del libro: "))
precio = int(input("Digite el precio del libro: "))
precio = float(input("Digite el precio del libro: ")
envioGratuito = input("Digite el envio gratuito: ")

if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    envioGratuito = "El valor es incorrecto,debe escribir True/False"
print(f'''
        nombre: {nombre}
        id: {id}
        precio: {precio}
        envioGratuito: {envioGratuito}
''')