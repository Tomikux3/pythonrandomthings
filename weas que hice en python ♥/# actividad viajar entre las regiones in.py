# actividad viajar entre las regiones indicadas

print('''
      Opciones de viaje :

      1- Copiapó
      2- Valparaiso
      3- Conceptión
      4- Puerto Montt

      ''')
# vvvvvv : notese que los "input" son "string" y las opciones elegidas en los "if" tambien son "string" esto ayuda a lanzar "else" en caso de ingresar numeros no ingresados y texto no ingresado !!
DestinoOrigen = (input('Ingrese el opción origen: '))
DestinoDestino = (input('Ingrese el opción destino: '))

if (DestinoOrigen == '1' and DestinoDestino == '1') or (DestinoOrigen == '2' and DestinoDestino == '2') or (DestinoOrigen == '3' and DestinoDestino == '3') or (DestinoOrigen == '4' and DestinoDestino == '4') :
    print(f'''
          Su viaje tiene un total de $0
          ''')
# vvvvvv : este "elif" abarca todos los resultados que dan $25.000, por eso es tan extenso !!
elif (DestinoOrigen == '1' and DestinoDestino == '2') or (DestinoOrigen == '2' and DestinoDestino == '1') or (DestinoOrigen == '3' and DestinoDestino == '2') or (DestinoOrigen == '2' and DestinoDestino == '3') or (DestinoOrigen == '3' and DestinoDestino == '4') or (DestinoOrigen == '4' and DestinoDestino == '3') :
    print(f'''
          Su viaje tiene un total de $25.000
          ''')
# vvvvvv : lo mismo pero con menos casos
elif (DestinoOrigen == '1' and DestinoDestino == '3') or (DestinoOrigen == '3' and DestinoDestino == '1') or (DestinoOrigen == '2' and DestinoDestino == '4') or (DestinoOrigen == '4' and DestinoDestino == '2') :
    print(f'''
          Su viaje tiene un total de $35.000
          ''')
elif (DestinoOrigen == '1' and DestinoDestino == '4') or (DestinoOrigen == '4' and DestinoDestino == '1') :
    print(f'''
          Su viaje tiene un total de $50.000
          ''')
else :
    print(f'''
          error: opción invalida
          ''')
print(f'''
          Adios y buen viaje !!
          ''')