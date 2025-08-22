class CuentaBancaria:
    def __init__(self, titular, num_cuenta, saldo=0):
        self.titular = titular
        self.num_cuenta = num_cuenta
        self.saldo = saldo 

    def consignacion(self, monto):
        self.saldo = self.saldo + monto
        print(f"Has consignado ${monto} a la cuenta {self.num_cuenta}.")
        print(f"Su saldo es de {self.saldo}.")

    def retiro(self, monto):
        if self.saldo >= monto:
            self.saldo = self.saldo - monto
            print(f"Has retirado ${monto} de la cuenta {self.num_cuenta}.")
            print(f"Su saldo restante es de {self.saldo}.")
        else:
            print("No cuenta con suficiente saldo.")

    def consultar_saldo(self):
        print(f"Su saldo total es {self.saldo}.")

cuenta = CuentaBancaria("Angelo", 23432984, 450000)
cuenta.consultar_saldo()
cuenta.consignacion(13000)
cuenta.retiro(500000)

