# listas
#var = 'peo'
#lista = [1, 'a', var, 2.5, [1, 2, 3]]
#nums = [1, 7, 5, 8, 15, 20]
#for num in nums :
    #print(num)
noms = ['Carlos', 'Juanita', 'Carlos', 'Federico', 'Bob'] # lista fuera del bucle para que se actualice
ruts = ['67420914-0', '69777420-1', '59481369-2', '74521874-3', '67632874-4']

try :
    while True :
        print(f'''
      *** MENU LISTA DE NOMBRES ***

      1- Agregar un nombre a la lista.
      2- Buscar rut / nombre.
      0- Salir. 
      ''')
        opc1 = int(input('Ingrese una opción valida del menu: '))
        if opc1 == 0 :
            print(f'Abandonando el programa. ')
            break
        elif opc1 == 1 :
            print(noms)
            nuevo_nom = input('Ingrese nuevo nombre: ')
            noms.append(nuevo_nom) # ".append()" es para agregar elemtentos a una lista
            for i in range(len(noms)) :
                print(f'indice {i} - posicion {i+1} - valor {noms[i]}\n')
            print(ruts)
            nuevo_rut = input('Ingrese nuevo rut: ')
            ruts.append(nuevo_rut) # ".append()" es para agregar elemtentos a una lista
            for i in range(len(ruts)) :
                print(f'indice {i} - posicion {i+1} - valor {ruts[i]}\n')
        elif opc1 == 2 :
            id = int(input('Ingrese el numero o indice del nombre / rut que desea saber: '))
            print(noms[id])
            print(ruts[id])
        else :
            print(f'error: Ingrese una opción valida. ')
except ValueError :
    print('error: Debe usar el tipo de variable correcta. ')
print(f'Hasta pronto !! ')

#search = input('Ingrese rut para buscar nombre: ')
#id2 = ruts.index(search)
#print[id2]