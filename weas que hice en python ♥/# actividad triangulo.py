# actividad triangulo
# genere un codigo que pida al usuario las medidas de un triangulo y luego se clasifique como: equilatero, isoceles o escoleno

print(f'''
      Bienvenido a el medidor de triangulos !!
      ''')

lado_a = float(input('Ingrese la medida A: '))
lado_b = float(input('Ingrese la medida B: '))
lado_c = float(input('Ingrese la medida C: '))

if lado_a == lado_b == lado_c : # la prueba logica mas restrictiva tiene que estar en el nivel superior
    print(f'''
          Es un triangulo " Equilátero "
          ''')
elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_c :
    print(f'''
          Es un triangulo " Isóceles "
          ''')
else : # La prueba logica menos restrictiva tiene que estar en el nivel inferior
    print(f'''
          Es un triangulo " Escoleno "
          ''')

print(f'''
      Fin del medidor de triangulos, adios !!
      ''')