# Ingrese palabra y encuentre valores unicos v2

palabra_ingr = input(f'Ingrese palabra: ')
unicos = ''
for letra in palabra_ingr:
    if not (letra in unicos):
        unicos = unicos   +   letra
print(unicos)