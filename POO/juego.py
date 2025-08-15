import random

def juego():

    numero = random.randint(1, 50)
    num_intentos = 5

    print("Intenta adivinar un número entre 1 y 50")

    for i in range(1, num_intentos+1):
        print(f"intento {i} de {num_intentos}")
        
        try:
            numero_2 = int(input("Ingresa un número: "))

        except ValueError:

            print("Ingresa un número entero válido")
            continue
        if numero_2 == numero:
            print("Has descubierto el número, ¡Felicidades!")
            print(f"¡Lo has adivinado en {i} intentos!")

        if numero_2 > numero:
            print ("El número es menor")

        if (numero_2 - numero) <= 2:
            print("Estás cerca")

        else:
            print("El número es mayor")

    print(f"Perdiste, el número es {numero}")
juego() 
