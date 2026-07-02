# Clinica Veterinaria
vets_regis = 0
consult_disp = 30
consult_agen = 0
consult_canc = 0
veterinario_senior = 0
veterinario_junior = 0
registro = ''

print(f'''
      === CLÍNICA VETERINARIA ===
      1- Registrar veterinario
      2- Ver consultas disponibles
      3- Agendar consulta
      4- Cancelar consulta
      5- Ver veterinarios registrados
      6- Salir
      ''')
while True :
    try :
        opc1 = int(input('Ingrese una opción valida: '))
        if opc1 == 6 :
            print(f'Saliendo del menú. ')
            break
        elif opc1 == 1 :
            print(f'Cuando ingrese su nombre debe tener un minimo de 6 caracteres y sin espacios. ')
            while True :
                vet = input('Ingrese su nombre: ')
                if (len(vet)) <= 5 or (' ' in vet) :
                    print('error: ¡Nombre inválido! Mínimo 6 caracteres y sin espacios. ')
                else :
                    print('Nombre registrado con exito. ')
                    vets_regis += 1
                    registro += vet
                    break
            while True :
                años = int(input('Ingrese años de experiencia: '))
                if años < 0 :
                    print(f'error: ¡Error de experiencia! Ingresa un número entero positivo. ')
                else :
                    print(f'Año/s registrado/s con exito. ')
                    registro += ' - ' + str(años)
                    if años > 5 :
                        print(f'Veterinario Senior registrado. ')
                        veterinario_senior += 1
                        registro += ' ' + '(Senior)\n'
                        break
                    elif años <= 5 :
                        print(f'Veterinario Junior registrado. ')
                        veterinario_junior += 1
                        registro += ' ' + '(Junior)\n'
                        break
        elif opc1 == 2 :
            if consult_disp == 0 :
                print(f'error: No hay consultas disponibles. ')
            else :
                print(f'Las consultas disponibles son: {consult_disp} ')
        elif opc1 == 3 :
            if consult_disp == 0 :
                print(f'error: No hay consultas disponibles. ')
            else :
                print(f'''Para agendar una consulta debe: 
                    ser una cantidad mayor a 0 
                    ser una cantidad menor o igual a {consult_disp} ''')
                consult_agen = int(input('Cuantas consultas desea agendar: '))
                if consult_agen <= 0 :
                    print(f'error: ¡Cantidad inválida! Debe ser un entero positivo.')
                elif consult_agen > consult_disp :
                    print(f'¡No hay suficientes consultas! Consultas disponibles: {consult_disp} ')
                else : 
                    consult_disp -= consult_agen
                    print(f'✓ Consulta agendada. Consultas restantes: {consult_disp} ')
        elif opc1 == 4 :
            if consult_agen == 0 :
                print(f'error: No hay consultas para cancelar. ')
            else : 
                print(f'Para cancelar consultas debe ingresar un numero mayor a 0 y menor a las consultas registradas. ')
                consult_canc = int(input('Cuantas consultas desea cancelar? : '))
                if consult_canc <= 0 :
                    print(f'error: ¡Cantidad inválida! Debe ser un entero positivo. ')
                elif consult_canc > consult_agen :
                    print(f'error: ¡No se pueden cancelar tantas! Consultas agendadas actualmente: {consult_agen} ')
                elif consult_canc >= 1 and consult_canc <= consult_agen :
                    consult_agen -= consult_canc
                    consult_disp += consult_canc
                    print(f'✓ Cancelación exitosa. Consultas disponibles: {consult_disp} ')
        elif opc1 == 5 :
            if registro == '' :
                print(f'error: aun no hay registro. ')
            else :
                print(f'''
                Veterinarios registrados: 
{registro}
                ''')
        else :
            print(f'error: ingrese una opción valida del menu. ')
    except ValueError :
        print(f'error: Debe ingresar un valor valido.')