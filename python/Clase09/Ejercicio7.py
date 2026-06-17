'''
Dadas las horas trabajadas de 5 personas y la tarifa de
pago,
calcular el saladio y la sumatoria de todos los salarios
'''

total_salario = 0
for i in range(1,6):
    print('persona',i)

    horas = float(input("Ingrese la cantidad de horas trabajadas: "))
    tarifa = float(input('Ingrese la tarifa por hora: '))

    salario = horas * tarifa
    print('El salario es: ',salario)
    total_salario += salario
    print('El salario total es: ',total_salario)
    print("")
    print('La suma de los salarios es: ',total_salario)
