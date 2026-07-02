# Farmacia Central

def Descuento_Receta():
    '''
    Función para aplicar descuento según tipo de receta.
    '''
    total = 0
    descuento = 0
    receta = 0
    tipo_receta = ''

    total = int(input('Ingrese total de la compra: '))
    tipo_receta = input('Ingrese el tipo de receta (A, B, o C): ')

    if tipo_receta == 'A' or tipo_receta == 'a' :
        descuento = 0.2 * total
    elif tipo_receta == 'B' or tipo_receta == 'b' :
        descuento = 0.1 * total
    else :
        descuento = 0

    total -= descuento
    print(f'Total a pagar: ${total}')

def Manejo_Stock():
    '''
    Función para descontar unidades vendidas.
    '''
    stockActual = 0
    cantidadVendida = 0
    stockActual = int(input('Stock disponible: '))
    cantidadVendida = int(input('Cantidad vendida: '))
    if cantidadVendida > stockActual :
        print(f'error: stock insuficiente. ')
    else :
        stockActual -= cantidadVendida
        print(f'Nuevo stock: {stockActual}')

