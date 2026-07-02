# calculadora basica
operación = input('inserte la operacion de matematica basica completa: ')
numeros = 0
mult = 1
div = 1
#operador = None
try :
    for car in operación :
        if car == '+' :
            if car in '1234567890' :
                car = int(car)
                numeros += car
        elif car == '-' :
            if car in '1234567890' :
                car = int(car)
                numeros -= car
    print(f'''
        Usted insertó: {operación}
        Y el resultado es: {numeros}
        ''')
except ZeroDivisionError :
    print('error: no se puede dividir en 0 ')