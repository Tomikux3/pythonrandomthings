# crear un cachipum

import random

print('''
      Cachipum !!
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
else :
     None
opc_usuario = str(input('Elige una opción: '))
if opc_usuario == '1' :
    opc_usuario = Pi
elif opc_usuario == '2' :
    opc_usuario = Pa
elif opc_usuario == '3' :
    opc_usuario = Ti
else :
     None
if ( opc_usuario == cpu ) :
    print('''
          Empate !!
          ''')
elif ( opc_usuario == Pi and cpu == Ti ) or (opc_usuario == Pa and cpu == Pi ) or (opc_usuario == Ti and cpu == Pa ) :
    print('''
          Ganaste !!
          ''')
elif ( opc_usuario == Pi and cpu == Pa ) or (opc_usuario == Pa and cpu == Ti ) or (opc_usuario == Ti and cpu == Pi ) :
        print('''
          Perdiste !!
          ''')
else :
        print('''
          error: Opción invalida :(
          ''')
print(f'Porque elegiste {opc_usuario} y la cpu eligió {cpu}')