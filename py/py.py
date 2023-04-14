



opcion = 0

while True :
    
    print('')

    print('BIENVENIDO A LA CALCULADORA')
    N1 = int(input('ingrese el primer numero'))
    N2 = int(input('ingrese el segundo numero'))

    print('')
    print('')
    print('ingrese el numero para seleccionar una opcion')
    print('ingrese 1 para sumar')
    print('ingrese 2 para restar')
    print('ingrese 3 para multiplicar')
    print('ingrese 4 si quiere cambiar lo numeros que ingreso para calcular')
    print('ingrese 5 para salir del programa')

    print('')
    opcion = int(input('elige la opcion al utilizar'))

    if opcion == 1:
        print(' el resultado es igual ala suma de n1 + n2 es:' , N1 + N2 )
    elif opcion == 2:
        print(' el resultado de los dos numeros al restar son:',N1 - N2)
    elif opcion == 3: 
        print('el resultado de la multipicasion de los dos numeros son:',N1 * N2)
    elif opcion == 4: 
        print('introducce nuevos numeros')
        N1 = int(input('ingrese el nuevo numero'))
        N2 = int(input('ingrese el segundo nuevo numero'))

    elif opcion == 5:
        break
    else:
        print('opcion incorrecta')




