# actividad temperatura
# genere un codigo que pida al usuario las medidas de un triangulo y luego se clasifique como: equilatero, isoceles o escoleno

print(f'''
      Bienvenido al medidor del clima !!
      ''')

temperatura = int(input('Ingrese la medida temperatura : '))
presión_atmos = int(input('Ingrese la presión atmosferica : '))

if 16 <= temperatura <= 30 and 11 <= presión_atmos <= 20 :
    print(f'''
          Es un dia " Caluroso "
          ''')
elif 0 <= temperatura <= 15 and 11 <= presión_atmos <= 20 :
    print(f'''
          Es un dia " Lluvioso "
          ''')
elif 16 <= temperatura <= 30 and 0 <= presión_atmos <= 10 :
    print(f'''
          Es un dia " Templado "
          ''')
elif 0 <= temperatura <= 15 and 0 <= presión_atmos <= 10 :
    print(f'''
          Es un dia " Frio "
          ''')
else :
    print(f'''
          error: Valores no clasificados
          ''')

print(f'''
      Fin del medidor de triangulos, adios !!
      ''')