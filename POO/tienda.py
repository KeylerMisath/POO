
def productos():
    saldo = int(input("Ingrese su saldo disponible: "))

    while True:
        print ("0. Terminar compra")
        print ("1. Aceite - 5000")
        print ("2. Arroz - 3000")
        print ("3. Azucar - 2000")
        print ("4. Sal - 1000")
        print ("5. Harina - 4000")
        print ("6. Carne - 15000")        
        
        opcion = input("Selecione los productos que desea comprar: ")

        match opcion:
            case "1":
                costo = 5000
                pago = saldo - costo
                ora = input(f"Has seleccionado Aceite. Su costo es {costo}. Su saldo restante es {pago}, ¿desea algo más?: ")
                if ora == "no":
                    break
            case "2":
                costo = 3000
                pago = saldo - costo
                ora = input(f"Has seleccionado Arroz. Su costo es {costo}. Su saldo restante es {pago}, ¿desea algo más?: ")
                if ora == "no":
                    break
            case "3":
                costo = 2000
                pago = saldo - costo
                ora = input(f"Has seleccionado Azúcar. Su costo es {costo}. Su saldo restante es {pago}¿desea algo más?: ")
                if ora == "no":
                    break
            case "4":
                costo = 1000
                pago = saldo - costo
                ora = input(f"Has seleccionado Sal. Su costo es {costo}. Su saldo restante es {pago}¿desea algo más?: ")
                if ora == "no":
                    break
            case "5":
                costo = 4000
                pago = saldo - costo
                ora = input(f"Has seleccionado Harina. Su costo es {costo}. Su saldo restante es {pago}¿desea algo más?: ")
                if ora == "no":
                    break
            case "6":
                costo = 15000
                pago = saldo - costo
                ora = input(f"Has seleccionado Carne. Su costo es {costo}. Su saldo restante es {pago}¿desea algo más?: ")
                if ora == "no":
                    break
            case "0":
                break
            case _:
                print("Opción no válida, por favor intente de nuevo.")
            
    saldo -= costo
    ora = input(f"Su saldo final es {saldo}. ¿Desea realizar otra compra? (si/no): ")
    if ora.lower() == "no":
        print("Gracias por su compra.")


        
productos()
            

