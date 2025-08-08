def sucesion_fibonacci():
    numero_inicial = 0
    numero_siguiente = 1
    for i in range(numero_inicial, 20, 1):
        numero_resultante = numero_inicial + numero_siguiente
        numero_inicial = numero_siguiente
        numero_siguiente = numero_resultante
        print(numero_resultante)

def calcular_seno():
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

def calcular_coseno():
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

while True:
    print("Seleccione una opción:")
    print("1. Sucesión de Fibonacci")
    print("2. Calcular Seno")
    print("3. Calcular Coseno")
    print("4. Salir")
    
    opcion = input("Ingrese su opción: ")
    
    if opcion == '1':
        sucesion_fibonacci()
    elif opcion == '2':
        calcular_seno()
    elif opcion == '3':
        calcular_coseno()
    elif opcion == '4':
        break
    else:
        print("Opción no válida, intente de nuevo.")
