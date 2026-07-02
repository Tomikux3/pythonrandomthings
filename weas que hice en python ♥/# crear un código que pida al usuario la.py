# crear un código que pida al usuario las medidas de rectángulo y le muestre el area y el perimetro

print(f'inserte las medidas del rectángulo: ')
medida_a1 = float(input('primera medida: '))
medida_b1 = float(input('segunda medida: '))
print(f'el área del rectángulo es de: {medida_a1*medida_b1:0.2f} metros cuadrados y el perímetro es de: {2*medida_a1 + 2*medida_b1:0.2f} metros ') 
# 0.2f es para limitar o forzar los decimales para las operaciones hechas dentro de {}