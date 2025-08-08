numero_x = float(input("Ingrese el valor en radianes:"))

cos = 0 
terminos = 20


for i in range (terminos):
    signo = (-1)**i
    numerador = numero_x ** (2*i)
    denominador = 1
    for j in range (1, 2*i+1):
        denominador = denominador * j
    signo_termino = signo * (numerador / denominador)
    cos = cos + signo_termino
print(f"El valor del coseno es: {cos}")
