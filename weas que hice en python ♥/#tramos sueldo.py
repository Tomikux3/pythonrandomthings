#tramos sueldo

print(f'tramos sueldo ')

sueldo=int(input('inserte sueldo: '))

if sueldo < 499999 :
    print(f' Nivel de sueldo "E" ')
elif (sueldo < 999999) :
    print(f'Nivel de sueldo "D" ')
elif (sueldo < 1499999) :
    print(f'Nivel de sueldo "C" ')
elif (sueldo < 1999999) :
    print(f'Nivel de sueldo "B" ')
else :
    print(f'Nivel de sueldo "A" ')

