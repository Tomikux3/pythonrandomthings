# contador de vocales
TsexT = input('Ingrese un texto: ')
cont_vocal = 0
for l in TsexT :
    if not l in 'qwrtypsdfghjklñzxcvbnm1234567890!"#$%&/()=¿?¡´+}{-.,;:_¨*[]' :
        cont_vocal += 1
print(f'{cont_vocal}')