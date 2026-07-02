# Actividad promediar notas
# Actividad indicar cantidad de notas a promediar - ingresar las notas y mostrar promedio

print(f'''
      Promediar notas !! 
      ''')

suma_notas = 0 # variable acumulativa
cant_notas = int(input('Ingrese la cantidad de notas a promediar: '))

for i in range(1 , cant_notas+1):
    notas = float(input(f'Ingrese {i}a nota: '))
    suma_notas += notas # actualización de variable acumulativa

promedio = (round(suma_notas / cant_notas)) # OJO a valores de BORDE
print(f'su promedio es : {suma_notas / cant_notas:0.1f} ')

if (promedio >= 4):
    print(f'Aprobado !!!')
else:
    print(f'Reprobado...')

print(f'''
      Adios y buena suerte !!
      ''')
