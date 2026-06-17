#En esta clase veremos la sentencia
'''
condicion = 10
if condicion == True:
    print('Condicion verdadera')
elif condicion == False:
    print('Condicion verdadera')
else:
    print('Condicion sin especificar')
'''
''''
num = int(input('Digite un numero en el rango de 1 al 3'))
numTexto = ''
if num == 1 :
    numTexto= 'numero uno'
elif num == 2 :
    numTexto= 'numero dos'
elif num == 3 :
    numTexto= 'numero tres'
else:
    numTexto= 'has ingredado un numero fuera de rango'
print(f'el numero ingresado es {num} - {numTexto}')
'''
condicion = True
#if condicion:
#    print('Condicion verdadera')
#else:
#    print('Condicion falsa')

print('condicion verdadera')if condicion else print('condicion falsa')
