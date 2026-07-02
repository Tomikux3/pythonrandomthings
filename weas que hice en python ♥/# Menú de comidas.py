# Menú de comidas

print(''' 
        Menú
        1- Carne
        2- Pescado
        0- Salir
        ''')

opc_ele = (input('Ingrese opción: '))

if opc_ele == '0' :
    print(f'Usted seleccionó: "Salir" ')
else :
    if opc_ele == '1' :
        print(f'Usted seleccionó: "Carne" ')
    else :
        if opc_ele == '2' :
            print(f'Usted seleccionó: "Pescado" ')
        else :
            print(f'Opción invalida ')

print(f' ')
print(f' ♥ Fin del menú ♥ ')
