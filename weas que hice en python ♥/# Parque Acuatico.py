# Parque Acuatico
# Sistema de reservas de Parque Acuatico

cupos_disp = 100
cupos_rese = 0
cupos_canc = 0

while True :
    try :
        print(f''' 
            *** MENU PRINCIPAL ***
          1- Ver cupos disponibles
          2- Reservar cupos
          3- Cancelar reserva
          4- Ver reservas realizadas
          5- Salir

          ''')
        opc1 = int(input('Seleccioné una opción: '))
        if opc1 == 5 :
            print(f'Saliendo del menu')
            break
        elif opc1 == 1 :
            print(f'La cantidad de cupos disponibles es de : {cupos_disp}. ')
        elif opc1 == 2 :
            print(f'Para reservar cupos debe ingresar un numero dentro del rango de 1 a {cupos_disp}. ')
            while True :
                try :
                    cupos_rese = int(input('Ingrese la cantidad a reservar: '))
                    if cupos_disp == 0 :
                        print(f'Ya no quedan cupos disponibles, por lo tanto, esta opción no está disponible. ')
                        break
                    elif cupos_rese > 0 and cupos_rese <= cupos_disp :
                        cupos_disp -= cupos_rese
                        print(f'Usted reservó {cupos_rese}, la cantidad de cupos disponibles ahora es de {cupos_disp}. ')
                        break
                    else :
                        print(f'error: No hay suficientes cupos disponibles, intentelo otra vez.')
                except ValueError :
                    print(F'error: Debe ingresar valores numericos enteros, intentelo otra vez. ')
        elif opc1 == 3 :
            print(f'Para cancelar reserva debe ingresar un numero dentro del rango de 1 a 100 y menor a los cupos que reservó. ')
            while True:
                try :
                    cupos_canc = int(input('Ingrese la cantidad a cancelar: '))
                    if cupos_rese == 0 :
                        print(f'Ya no quedan cupos para cancelar, por lo tanto, esta opción no está disponible. ')
                        break
                    elif cupos_canc > 0 and cupos_canc <= cupos_rese :
                        cupos_disp += cupos_canc
                        print(f'Usted canceló {cupos_canc}, la cantidad de cupos disponibles ahora es de {cupos_disp}. ')
                        break
                    else :
                        print(f'error: No hay suficientes cupos para cancelar, intentelo otra vez. ')
                except ValueError :
                    print(F'error: Debe ingresar valores numericos enteros, intentelo otra vez. ')
        elif opc1 == 4 :
            if cupos_rese == 0 :
                print(f'No hay cupos reservados. ')
            else :
                print(f'La cantidad de cupos reservados es de {cupos_rese-cupos_canc}. ')
        else : 
            print(f'error: opción no disponible, ingrese una opción valida del menu. ')
    except ValueError :
        print(f'error: Debe ingresar valores numericos enteros, intentelo otra vez. ')
print(f'Gracias por visitar Splash World, Hasta pronto !! ')