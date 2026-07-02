# Instancia de decision (if - elif - else)

# "or" es permisivo
# "and" es restrictivo
# True = 1
# False = 0

# separador - separador - separador - separador - separador - separador - separador - separador - separador - separador - separador - separador.

# "if" (Prueba Logica): 
#   Acciónes verdaderas
# else:
#   Acciónes falsas

# separador - separador - separador - separador - separador - separador - separador - separador - separador - separador - separador - separador.

# Solicitar al usuario su asistencia y su nota: determine si aprueba o reprueba

print(f'aprueba o no aprueba :) ')
nota_final_uno = float(input('Inserte su nota final: '))
asistencia_final_uno = float(input('Inserte su porcentaje de asistencia final: '))
if (nota_final_uno >= 4.0) and (asistencia_final_uno >= 75.0) :
    print(f'Aprobaste. Felicidades nos vemos el proximo semestre ☻ !!')
else :
    print(f'Reprobaste. Nos vemos el proximo semestre ☺ !!')


