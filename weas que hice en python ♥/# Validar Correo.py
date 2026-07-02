# Validar Correo
# incluir 'try' y 'except'
# hacerlo menu
print('''
      1- Ingresar correo
      2- Mostrar correos validos
      3- Salir
      ''')
while True :
    opc1 = int(input('Ingrese opcion: ')) # pide y almacena la opcion del menu 
    if opc1 == 1 :
        while True :
            correo = input('Ingrese correo: ') # pide y almacena el correo
            arroba = False
            punto = False
            duocuc = False
            valido = False
            numeros = False
            Largo = 0
            contpuntos = 0
            nom = ''
            dom = ''
            for l in correo : # "for" que separa el nombre y el dominio del correo
                if l == '@' : arroba = True
                if not arroba :
                    nom = nom + l # almacena el nombre del correo
                else :
                    dom = dom + l # almacena el dominio del correo
            for l in correo :
                if l in 'duocuc.cl' : duocuc = True # verifica que el correo tenga el dominio 'duocuc.cl'
            for l in correo :
                if l in '1234567890!"#$%&/()=?¿¡/*-+' : # verifica que el correo no tenga numeros ni caracteres especiales
                    numeros = True
                    print('error: nombre no valido')
            for l in nom : # contador de letras
                Largo += 1
            for l in nom : # contador de puntos
                if l == '.' :
                    contpuntos += 1
            if contpuntos == 1 : # verifica que el nombre del correo tenga un solo punto
                punto = True
            if not punto :
                print('error: no hay punto')

            print(nom)
            print(dom)
            print(Largo)

            #print(nom+dom)

            if (punto) and (duocuc) and (arroba) and (Largo == 10) and (not numeros) :
                valido = True
            # ^^^^^^ variables que se esperan que sean 'True' en una prueba logica se deja por si sola
            # ^^^^^^ variables que se esperan que sean 'False' se verifica con un 'not' seguido de la variable
            if valido == True :
                print(f'correo valido ')
                correo = correo + ' | ' 
            else :
                print(f'correo no valido ')
            opc2 = input('Desea ingresar otro correo? | 1- Si | 2- No | : ')
            try :
                if opc2 == '1' :
                    continue
                elif opc2 == '2' :
                    break
            except :
                print('error: Opcion no valida, saliendo del programa ')
                break
    elif opc1 == 2 :
        while True :
            try :
                print(f'''
                    Correos validos son : 
                      {correo}
                    ''')
                print(f'{correo}')
            except NameError :
                print('No hay correos validos para mostrar ')
            break
    elif opc1 == 3 :
        print('Saliendo del programa, gracias por su visita ')
        break

