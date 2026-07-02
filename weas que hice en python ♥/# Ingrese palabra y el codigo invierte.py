# Ingrese palabra y el codigo invierte

palabra_ingr=input(f'Ingrese palabra: ')
inv = ''
for palabra in palabra_ingr:
    inv = palabra   +   inv
print(inv)