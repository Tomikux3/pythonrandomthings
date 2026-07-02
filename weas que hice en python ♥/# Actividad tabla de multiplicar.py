# Actividad: tabla de multiplicar

print('''
    Tabla de multiplicar :D
       ''')
mult_user =  int(input('Inserte el numero del que desea la tabla: ')) # comando para el usuario
print(f' ')

for i in range(1 , 13): # bucle que llega del 1 al 13-1 (12)
    print(f'{mult_user} x {i} = {mult_user * i}')

print('''
      Fin de la tabla ♥
      ''')
