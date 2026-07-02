# Menu de notas y promediar
print(f'''
      Bienvenido a la calculadora de notas V2 !!!
      ''')
var_acu_notas = 0.0 # valores acumulativos
var_acu_cantnotas = 0
while True : # menu "while": al ser siempre "True" ingresas sin necesidad de condicion
    try :
        print('''
        ------------------------------------------------------------
            
        Menú
        1- Ingresar Nota
        2- Calcular promedio
        3- Salir
            
        ------------------------------------------------------------
        ''')
        opc_ele1 = int(input('''
                        Eliga una opción:
                        '''))
        if opc_ele1 == 3 :
            print(f'Abandonó el menú')
            break
        elif opc_ele1 == 1 :
            while True :
                try :
                    notas = float(input('Ingrese la nota: '))
                    if notas >= 1 and notas <= 7 :
                        var_acu_notas = var_acu_notas + notas
                        var_acu_cantnotas += 1
                        print(f'Nota ingresada :D ')
                        break
                    else :
                        print('''
            error: Debe ingresar una nota entre 1 y 7.
                            ''')
                except ValueError :
                    print(f'''
            error: Ingrese un numero de nota valido. 
              ''')
        elif opc_ele1 == 2 :
            try : 
                (var_acu_notas / var_acu_cantnotas)
            except ZeroDivisionError :
                print(f'''
            error: Aun no ingresó notas, no se puede dividir en 0.
                    ''')
            else :
                print(f'Su promedio es {var_acu_notas / var_acu_cantnotas:0.1f}')
    except ValueError :
        print(f'''
            error: Ingrese una de las opciones validas. (1, 2, 3.) 
              ''')

