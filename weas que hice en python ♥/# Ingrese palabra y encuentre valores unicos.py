# Ingrese palabra y encuentre valores unicos

palabra_ingr = input(f'Ingrese palabra: ')
unicos = ''
for letra in palabra_ingr:
    if letra in unicos:
        continue # acción vacía para que el codigo avance
    else:
        unicos = unicos   +   letra
print(unicos)