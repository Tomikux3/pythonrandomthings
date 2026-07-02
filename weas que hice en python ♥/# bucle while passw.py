# bucle while
passw = '123'
intentos = 1
while intentos <= 3 :
    passw_ing = input('Ingrese contraseña: ')
    if passw_ing == passw :
        print(f'correcta')
        intentos += 1
        break
    else:
        print('incorrecta')
        if intentos == 3 :
            print('contraseña bloqueada')
        intentos += 1