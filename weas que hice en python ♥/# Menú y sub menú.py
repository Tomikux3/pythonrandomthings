#  Menú y sub menú
print('''
    1- Trauma 
    2- Cardio 
    3- Pediatría
    ''')

opc_ele1 = (input('Ingrese especialidad: '))
if opc_ele1 == '1' :
    print(f'Usted seleccionó "Trauma" ')
    print('''
    1- Dr. Perez
    2- Dra. Gonzalez
    3- Dr. Soto
    ''')
    opc_ele2 = (input('Seleccione Doctor/a: '))
    if opc_ele2 == '1' :
        print(f'Usted seleccionó a: "Dr. Perez" ')
    elif opc_ele2 == '2' :
        print(f'Usted seleccionó a: "Dra. Gonzalez" ')
    elif opc_ele2 == '3' :
        print(f'Usted seleccionó a: "Dr. Soto" ')
    else :
        print(f'Opción invalida ')
elif opc_ele1 == '2' :
    print(f'Usted seleccionó "Cardio" ')
    print('''
    1- Dra. Zuñiga
    2- Dr. Luna
    3- Dr. Mengueche
    ''')
    opc_ele2 = (input('Seleccione Doctor/a: '))
    if opc_ele2 == '1' :
        print(f'Usted seleccionó a: "Dra. Zuñiga" ')
    elif opc_ele2 == '2' :
        print(f'Usted seleccionó a: "Dr. Luna" ')
    elif opc_ele2 == '3' :
        print(f'el que te llenó el culo de leche')
    else :
        print(f'Opción invalida ')
elif opc_ele1 == '3' :
    print(f'Usted seleccionó "Pediatría" ')
    print('''
    1- Dr. Diaz
    2- Dr. Abarca
    3- Dra. Machuca
    ''')
    opc_ele2 = (input('Seleccione Doctor/a: '))
    if opc_ele2 == '1' :
        print(f'Usted seleccionó a: "Dr. Diaz" ')
    elif opc_ele2 == '2' :
        print(f'Usted seleccionó a: "Dr. Abarca" ')
    elif opc_ele2 == '3' :
        print(f'Usted seleccionó a: "Dra. Machuca" ')
    else :
        print(f'Opción invalida ')
else :
    print(f'Opción invalida ')

print(f' ♥ Fin de la atención ♥ ')
