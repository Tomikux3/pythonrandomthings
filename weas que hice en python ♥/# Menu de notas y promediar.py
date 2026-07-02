# Menu de notas y promediar
print(f'''
      Bienvenido a la calculadora de notas V2 !!!
      ''')
var_acu_notas = 0.0
var_acu_cantnotas = 0
while True :
    print('''
      ------------------------------------------------------------
          
      Menú
      1- Ingresar Nota
      2- Calcular promedio
      3- Salir
          
      ------------------------------------------------------------
      ''')
    opc_ele1 = (input('''
                      Eliga una opción:
                      '''))
    if opc_ele1 == '3' :
        print(f'Abandonó el menú')
        break
    elif opc_ele1 == '1' :
        notas = float(input('Ingrese la nota: '))
        var_acu_notas = var_acu_notas + notas
        var_acu_cantnotas += 1
        print(f'Nota ingresada :D ')
    elif opc_ele1 == '2' :
        if var_acu_cantnotas == 0:
            print(f'Aun no ingresó notas')
        else:
            print(f'Su promedio es {var_acu_notas / var_acu_cantnotas:0.1f}')
    else :
        print(f'Opción invalida, intente nuevamente')