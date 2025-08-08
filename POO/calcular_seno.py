numero_x = float(input("Ingrese el valor en radianes:"))

sen = 0 
terminos = 20

for i in range (terminos):
    signo = (-1)**i
    numerador = numero_x ** (2*i+1)
    denominador = 1
    for j in range (1, 2*i+2):
        denominador = denominador * j
        signo_termino = signo * (numerador / denominador)
        sen = sen + signo_termino
print(f"El valor del seno es: {sen}")
