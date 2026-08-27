'''
Ejercicio02:Determinar la solución lógica de la siguiente expresion
    ((3+5+8)<3 and ((-6/3*4)+2<2) or (a>b)
    1-Pedir al usuario los dos valores para a y b
    2_Escribir en coódigo la siguiente expresion
    3-mostrar el resultado
'''

a=float(input("digite el valor para a:"))
b=float(input("digite el valor para b:"))
resultado = ((3+5+8)<3 and ((-6/3*4)+2<2) or (a>b))
print(f"el resultado es: {resultado}")

