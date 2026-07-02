
# genere un codigo que le permita al usuario promediar 3 notas

pri_nota = float(input("Ingrese la primera nota: "))
seg_nota = float(input("Ingrese el segunda nota: "))
ter_nota = float(input("Ingrese el tercera nota: "))
cant_notas = float(input("Ingrese la cantidad de notas: "))
# prom_nota = round((pri_nota+seg_nota+ter_nota)/3,1)
# print(f'el promedio de los numeros ingresados es: {prom_nota}')
print(f'el promedio de los numeros ingresados es: {(pri_nota + seg_nota + ter_nota) / cant_notas:0.1f}')
print(f' ♥ mish ♥ ')