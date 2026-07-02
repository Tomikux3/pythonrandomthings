# contraseña 3 intentos
print('''
      Bienvenido a www.MySocialBookNet420.com
      Usted inició sesión como " Dr. Mengueche "
      ''')
passw = 'patapeo3636'
for i in range(3):
    ingr_passw=input(f'Ingrese la contraseña: ')
    if passw == ingr_passw:
        print(f'contraseña correcta, bienvenido " Dr. Mengueche "')
        break # "break" para romper el bucle bajo ciertas condiciones (va dentro del if)
    else:
        print(f'contraseña invalida, intentelo nuevamente')
        if i == 2: print('cuenta bloqueada: intentos maximos alcanzados !')