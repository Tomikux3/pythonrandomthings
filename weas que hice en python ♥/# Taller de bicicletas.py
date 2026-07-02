# Taller de bicicletas

# 'codigo_del_repuesto' : ['nombre_del_repuesto', cantidad_en_stock, precio_unitario]
inventario = {
    'R001': ['Cadena', 25, 15.99],
    'R002': ['Freno de disco', 12, 45.50],
    'R003': ['Cámara de aire', 40, 8.75],
    'R004': ['Lubricante', 18, 12.30],
    'R005': ['Casco urbano', 8, 35.00]
}

print('''
        ╔══════════════════════════════════════════╗
        ║     CICLOREPUESTOS MASTER - INVENTARIO   ║
        ╠══════════════════════════════════════════╣
        ║  1. 🆕 Agregar repuesto                  ║
        ║  2. 🔍 Buscar repuesto                   ║
        ║  3. 📦 Actualizar stock                  ║
        ║  4. ❌ Eliminar repuesto                 ║
        ║  5. 📋 Mostrar todo el inventario        ║
        ║  6. ⚠️  Repuestos con bajo stock          ║
        ║  7. 💰 Valor total por categoría         ║
        ║  8. 🚪 Salir                             ║
        ╚══════════════════════════════════════════╝
      ''')
try :
    opc1 = int(input('Ingrese una opción del menú: '))
    if opc1 == 8 :
        print('Saliendo del menú')
        #break
    elif opc1 == 1 :
        codigo_repuesto = input('Ingrese el codigo del repuesto: ')
        if codigo_repuesto in 'xX' :
            print(f'Saliendo del sub-menú. ')
            #break
        elif codigo_repuesto in inventario :
            print(f'error: el codigo ya existe en el inventario.')
            #break
        else :
            nombre = input('Ingrese el nombre del repuesto: ')
            cantidad = int(input('Ingrese la cantidad del repuesto: '))
            precio = float(input('Ingrese el precio del repuesto: '))
            if (len(codigo_repuesto) > 0) and (codigo_repuesto[0] == 'R') and (len(nombre) > 0 ) and (cantidad > 0) and (precio > 0) :
                inventario[codigo_repuesto] = [nombre, cantidad, precio]
                print(inventario)
            else :
                print(f'error: datos ingresados invalidos. ')
    elif opc1 == 2 :
        print(f'Desea buscar por nombre o por codigo?')
        opc2 = int(input('1- Nombre | 2- Codigo | 8- Salir '))
        if opc2 == 8 :
            print(f'Saliendo de la opción. ')
        elif opc2 == 1 :
            nombre_buscar = input('ingrese el nombrar para buscar: ')
            print(inventario[nombre_buscar])
        elif opc2 == 2 :
            codigo_buscar = input('Ingrese el codigo para buscar: ')
            print(inventario[codigo_buscar])
        else :
            print(f'error: debe ingresar una opción valida del menú. ')
    else :
        print(f'error: debe ingresar una opción valida del menú. ')
except ValueError :
    print(f'error: tipo de valor invalido. ')
except KeyError :
    print(f'error: codigo inexistente. ')