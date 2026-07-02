# crear un cachipum

import random

wins_user = 0 # variable acumulativa para acumular las victorias del usuario
wins_cpu = 0 # variable acumulativa para acumular las victorias de la cpu
Truentera = True # banderilla para el "while"
print('''
      Cachipum !!
      
      El primero en llegar a X cantidad de victorias gana.
      ''')
cant_wins_needed = int(input('Cuantas victorias serán necesarias? : ')) # variable que fija con cuantas victorias acabará el bucle "while"
while Truentera : # bucle
    if wins_user == cant_wins_needed : # si el usuario llega a la cantidad designada anteriormente se considera victoria
        print(f'''
              Felicidades usuario ganaste contra la cpu !!
              Ganaste por {wins_user} a {wins_cpu} victorias
              ''')
    elif wins_cpu == cant_wins_needed : # si la cpu llega a la cantidad designada anteriormente se considera derrota
        print(f'''
              Que lastima... perdiste contra la cpu !! 
              Perdiste por {wins_cpu} a {wins_user} victorias
              ''')
    if wins_user == cant_wins_needed or wins_cpu == cant_wins_needed : # se rompe el bucle si cualquiera de los 2 llegan a la cantidad designada
        break
    print('''
        1- Piedra
        2- Papel
        3- Tijeras
        ''')
    Pi = 'Piedra'
    Pa = 'Papel'
    Ti = 'Tijeras'
    cpu = random.randint(1, 3)
    if cpu == 1 :
        cpu = Pi
    elif cpu == 2 :
        cpu = Pa
    elif cpu == 3 :
        cpu = Ti
    opc_usuario = str(input('Elige una opción: ')) # "input" para jugar
    if opc_usuario == '1' :
        opc_usuario = Pi
    elif opc_usuario == '2' :
        opc_usuario = Pa
    elif opc_usuario == '3' :
        opc_usuario = Ti
    if ( opc_usuario == cpu ) :
        print('''
            Empate !!
            ''')
    elif ( opc_usuario == Pi and cpu == Ti ) or (opc_usuario == Pa and cpu == Pi ) or (opc_usuario == Ti and cpu == Pa ) :
        print('''
            Ganaste !!
            ''')
        wins_user = wins_user + 1 # acumulación
    elif ( opc_usuario == Pi and cpu == Pa ) or (opc_usuario == Pa and cpu == Ti ) or (opc_usuario == Ti and cpu == Pi ) :
        print('''
            Perdiste !!
            ''')
        wins_cpu = wins_cpu + 1 # acumulación
    else :
        print('''
        error: Opción invalida :(
        ''')
    print(f'Porque elegiste {opc_usuario} y la cpu eligió {cpu}')
    print(f'''
          Victorias usuario: {wins_user}
          Victorias cpu: {wins_cpu}
          ''')
print(f'''
      Fin del cachipum !!
      ''')