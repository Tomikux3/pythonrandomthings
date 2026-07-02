# Actividad: El programa generará un número aleatorio y lo ajustará para que sea par, luego el jugador deberá adivinarlo en 3 intentos.

import random

print('''
      Juego:
      Adivinar el numero par generado aleatoriamente

      el primer numero será el limite inicial
      el segundo numero será el limite final

      (nota: cuando ingrese los numeros, el primero debe ser menor al segundo)
      ''')

num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))

if num1 << num2 :
    cpu = random.randint(num1, num2)
    print(f'numeros {num1} y {num2} ingresados exitosamente !! ')
    if (cpu % 2) == 0 :
        num_cercano_abajo = cpu
    else :
        num_cercano_abajo = cpu - 1
    # print(f'cpu = {cpu} | num cercano = {num_cercano_abajo}')
    user_guess1 = int(input('Adivina el numero: '))
    if  user_guess1 == num_cercano_abajo :
        print('''
              Adivinaste el numero, Felicidades !!
              ''')
    elif user_guess1 != num_cercano_abajo :
        print(f'Numero equivocado, intentalo nuevamente !! ')
        user_guess2 = int(input('Adivina el numero: '))
        if user_guess2 == num_cercano_abajo :
            print('''
                  Adivinaste el numero, Felicidades !!
                  ''')
        else :
            print(f'Numero equivocado, intentalo nuevamente !! ')
            user_guess3 = int(input('Adivina el numero: '))
            if user_guess3 == num_cercano_abajo :
                print('''
                      Adivinaste el numero, Felicidades !!
                      ''')
            else :
                print(f'Numero equivocado. Suerte para la proxima !! ')
                print(f'El numero era {num_cercano_abajo} !!')
elif num1 >> num2 :
    print(f'error: {num1} es mayor a {num2}. por favor vuelve a ejecutar el codigo. ')
else :
    print(f'error: datos ingresados no validos, por favor vuelve a ejecutar el codigo. ')