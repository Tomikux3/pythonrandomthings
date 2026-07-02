# actividad Genere un numero aleatorio entre 1 y 10
import random
print('''
      Adivine un numero del 1 al 10
      ''')
cpu_pick = random.randint(1, 10)
user_guess = int(input('Cual es tu elección? : '))

print(f'Tu elección es: " {user_guess} " y el numero que debió elegir es: " {cpu_pick} " ')

if (user_guess == cpu_pick) :
    print('''
          Acertaste, Felicidades !! 
          ''')
elif (user_guess != cpu_pick) and (cpu_pick > user_guess) :
        print('''
          No acertaste, Buen intento !! 
          ''')
        print('''
          Muy Bajo !! 
          ''')
elif (user_guess != cpu_pick) and (cpu_pick < user_guess) :
        print('''
          No acertaste, Buen intento !! 
          ''')
        print('''
          Muy Alto !! 
          ''')
else :
         print('''
          error: Elección invalida !! 
          ''')