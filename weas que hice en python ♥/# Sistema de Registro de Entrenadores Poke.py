# Sistema de Registro de Entrenadores Pokemon

print(f'\nBienvenido al Sistema de Registro de Entrenadores Pokémon')

# 'len' sirve para contar los caracteres de un 'string'
# ejemplo : len(azul) ---> 4

maestros_pokemon = 0
entrenador_novato = 0
cant_medallas = 0
cont_bucles = 0
cont_bucles2 = 0
while True :
    try :
        cant_entrenadores = int(input('Cuántos entrenadores se registrarán ?: '))
        if cant_entrenadores <= 0 :
            print(f'error: Cantidad invalida. Vuelve a intentarlo ')
        else :
            for i in range(cant_entrenadores) :
                try :
                    print('''
                        Requisitos:
                        
                    - Nombre de entrenador
                    - Minimo 6 caracteres
                    - No puede contener espacios.
                        ''')
                    # if (lent(entrenador_pokemon)<=5) or (' ' in entrenador_pokemon): print('nombre invalido')
                    # for i in range(cant) | para que no avance el bucle "for" usar "i-1"
                    entrenador_pokemon = input('Ingrese su nombre de entrenador: ') 
                    espacio = False
                    min_caract = False
                    cont_letras = 0
                    for l in entrenador_pokemon :
                        cont_letras += 1
                        if cont_letras >= 6 :
                            min_caract = True
                        if l == ' ' :
                            espacio = True
                    if (min_caract) and (not espacio) :
                        print('Nombre de entrenador ingresado correctamente. ')
                        cont_bucles += 1
                    else :
                        print('error: Nombre invalido. Intente nuevamente. ')
                        i-1 # step back
                        continue
                    cant_medallas = int(input('Ingrese su cantidad de medallas: '))
                    if cant_medallas <= 0 :
                        print('Cantidad invalida ')
                        cant_medallas = 0
                        i-1
                        continue
                    else :
                        print('Cantidad de medallas ingresada. ')
                        if cant_medallas > 8 :
                            print('Ingresado en la sección: Maestros Pokemon')
                            maestros_pokemon += 1
                            cont_bucles2 += 1
                        else : 
                            print('Ingresado en la sección: Entrenadores Novatos')
                            entrenador_novato += 1
                            cont_bucles2 += 1
                except ValueError :
                    print('error: Debe ingresar un numero entero valido. ')
                    i - 1
                    continue
            break
    except ValueError :
        print('error: Debe ingresar un numero entero valido. ')

print(f'''
      Se registraron: 
      {maestros_pokemon}   Maestro/s Pokémon 
      {entrenador_novato}  Entrenador/es Novato
      ''')