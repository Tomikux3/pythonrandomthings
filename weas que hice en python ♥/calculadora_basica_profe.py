# calculadora basica profe
suma = 0
resta = 0
multi = 1
div = 1
texto = input('Ingrese texto: ')
try :
    if '*' in texto:
        for letra in texto:
            if letra != '*':
                multi *= int(letra)
        print(multi)
    if '/' in texto:
        for letra in texto:
            if letra != '/':
                div = (1/int(letra))/div
        print(div)
    if '+' in texto:
        for letra in texto:
            if letra != '+':
                suma += int(letra)
        print(suma)
    elif '-' in texto:
        for letra in texto:
            if letra != '-':
                resta = (int(letra)-resta)
        print(-1*resta)
except ZeroDivisionError :
    print('error: no puedes dividir con 0 ')