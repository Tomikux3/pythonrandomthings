# Gimnasio Municipal
print('''
      Bienvenido al Gimnasio Municipal
      ''')
Membresia_Mensual_base = 20000
Membresia_Mensual = 20000
Botella_Deportiva_base = 6000
Botella_Deportiva = 6000
descuento = 0
descuento2 = 0
Dias_Asist = int(input('Cuantos dias del mes asistió? : '))
Adulto_Mayor = (input('Usted es adulto mayor? | 0 = No | 1 = Si | : '))

if Dias_Asist >= 10 and Dias_Asist < 20 and Adulto_Mayor == '0' :
    descuento = 10
    Membresia_Mensual = Membresia_Mensual * (1 - (descuento / 100))
elif Dias_Asist >= 10 and Dias_Asist < 20 and Adulto_Mayor == '1' :
    descuento = 18
    Membresia_Mensual = Membresia_Mensual * (1 - (descuento / 100))
elif Dias_Asist >= 20 and Adulto_Mayor == '0' :
    descuento = 20
    Membresia_Mensual = Membresia_Mensual * (1 - (descuento / 100))
elif Dias_Asist >= 20 and Adulto_Mayor == '1' :
    descuento = 30
    Membresia_Mensual = Membresia_Mensual * (1 - (descuento / 100))
elif Dias_Asist <= 9 and Adulto_Mayor == '1' :
    Membresia_Mensual = Membresia_Mensual
elif Dias_Asist <= 9 and Adulto_Mayor == '0' :
    Membresia_Mensual = Membresia_Mensual
else :
    print('''
          error: valores ingresados no validos
          ''')

if Dias_Asist >= 15 and Adulto_Mayor == '0' :
    descuento2 = 5
    Botella_Deportiva = Botella_Deportiva * (1 - (descuento2 / 100))
elif Dias_Asist < 15 and Adulto_Mayor == '1' :
    descuento2 = 12
    Botella_Deportiva = Botella_Deportiva * (1 - (descuento2 / 100))
elif Dias_Asist >= 15 and Adulto_Mayor == '1' :
    descuento2 = 17
    Botella_Deportiva = Botella_Deportiva * (1 - (descuento2 / 100))
elif Dias_Asist < 15 and Adulto_Mayor == '0' :
    Botella_Deportiva = Botella_Deportiva

else :
    print('''
          error: valores ingresados no validos
          ''')

print(f'''
        Membresia:  ${Membresia_Mensual_base} - {descuento}% = ${(Membresia_Mensual):0.0f}
        Botella:    ${Botella_Deportiva_base} - {descuento2}% = ${(Botella_Deportiva):0.0f}
        Total:      ${(Membresia_Mensual + Botella_Deportiva):0.0f}
        ''')