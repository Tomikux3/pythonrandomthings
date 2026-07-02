# Actividad ejercicio para prueba

print(f' Menú: tarjeta de credito ')

# vvvvvv variables acumulativas base

deuda = 100000
tarjeta_credito = -100000
sumas_compras = 0

# vvvvvv banderillas que permiten que los dos "while" funcionen

Truentera1 = True
Truentera2 = True

while Truentera1 : # primer menú
    print(f'''
      Menú
      1- Pago de Credito
      2- Comprar
      3- Salir
      ''')
    opc_ele1 = input('''
                     Ingrese una opción:
                     ''')
    if opc_ele1 == '3' :
        print(f'Cierre de menú ') # salida del bucle
        break
    elif opc_ele1 == '1':
        print(f'su deuda es de: ${deuda} a pagar')
        pago = int(input('Ingrese la cantidad que desea pagar: '))
        if pago >= 0 and pago >= tarjeta_credito :
            tarjeta_credito += pago
            deuda -= pago
            print(f'pagó: ${pago}, su deuda restante es: ${deuda} ')
        else :
            print('''
                  error: valor invalido
                  ''')
    elif opc_ele1 == '2' :
        while Truentera2 : # sub menú
            print('''
                  1- Comprar
                  3- Salir
                  ''')
            opc_ele2 = input('''
                             Ingrese una opción:
                             ''')
            if opc_ele2 == '3' :
                print(f'Cierre de menú') # salida de sub bucle
                break
            elif opc_ele2 == '1' :
                print(f'Seleccionó "Comprar" ')
                monto = int(input('Ingrese el monto: '))
                if monto >= 0 :
                    deuda += monto
                    sumas_compras += monto
                    tarjeta_credito -= monto
                    print(f'su total de compras es: ${sumas_compras}, y su nuevo saldo es: ${tarjeta_credito} ')
    else :
        print('''
              error: opción invalida
              ''')
