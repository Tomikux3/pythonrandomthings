# Ingresar Rut y Nombre

dicc_rutnom = {} # diccionario fuera del bucle
try :
    while True :
        print('''
            *** MENU ***
            1- Ingresar datos.
            2- Buscar rut y/o nombre.
            0- Salir.
            ''')
        opc1 = int(input('Ingrese una opción del menu: '))
        if opc1 == 0 :
            print('Saliendo del menu')
            break
        elif opc1 == 1:
            while True :
                rut = input('Ingrese rut, para salir ingrese "x" : ')
                if rut in 'xX' : # ingresar "x" para romper el sub bucle
                    print(f'Saliendo del sub-menu. ')
                    break
                elif rut in dicc_rutnom : # si se ingresa un rut que ya existe en el diccionario se rompe el bucle.
                    print(f'error: este rut ya se encuentra dentro de la base de datos. ')
                    break
                else :
                    nombre = input('Ingrese su nombre: ')
                    tel = input('Ingrese su telefono :')
                    edad = input('Ingrese su edad :')
                    peso = input('Ingrese su peso :')
                    estatura = input('Ingrese su estatura :')
                    # vvvvv aqui se agregan variables al diccionario
                dicc_rutnom[rut] = {'nombre' : nombre, 'telefono' : tel, 'edad' : edad, 'peso' : peso, 'estatura' : estatura}
                print(dicc_rutnom)
                #for coso in dicc_rutnom :
                    #print(f'RUT: {coso} | Nombre: {dicc_rutnom[coso]}')
        elif opc1 == 2 :
            rut_buscar = input('Ingrese el rut para buscar: ')
            print(dicc_rutnom[rut_buscar]['nombre'])
            print(dicc_rutnom[rut_buscar]['telefono'])
            print(dicc_rutnom[rut_buscar]['edad'])
            print(dicc_rutnom[rut_buscar]['peso'])
            print(dicc_rutnom[rut_buscar]['estatura'])
        else :
            print('error: Debe ingresar una opción valida del menu. ')
except (KeyError) :
    print(f'error: Rut no encontrado. ')
except (ValueError) :
    print(f'error: debe ingresar el tipo de variable correcta. ')
except rut in dicc_rutnom :
    print(f'error : este rut ya se encuentra dentro de la base de datos. ')