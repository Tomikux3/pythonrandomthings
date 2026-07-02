# Menú de comidas

print(''' 
        Menú
        1- Carne
        2- Pescado
        3- Pollo
        4- Verdura
        0- Salir
        ''')

opc_ele = (input('Ingrese opción: '))

if opc_ele == '0' :
    print(f'Usted seleccionó: "Salir" ')
elif opc_ele == '1' :
    print(f'Usted seleccionó: "Carne" ')
elif opc_ele == '2' :
    print(f'Usted seleccionó: "Pescado" ')
elif opc_ele == '3' :
    print(f'Usted seleccionó: "Pollo" ')
elif opc_ele == '4' :
    print(f'Usted seleccionó: "Verdura" ')
else :
    print(f'Opción invalida ')

print(f' ')
print(f' ♥ Fin del menú ♥ ')
