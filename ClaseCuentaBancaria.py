class CuentaBancaria:

    def __init__(self, titular, saldo=0.0):
        # saldo=0.0 es el valor por defecto si no se indica otro
        self.titular = titular
        self.saldo   = saldo

    def depositar(self, monto):
        if monto <= 0:
            print("Monto invalido: debe ser mayor a cero.")
            return
        self.saldo += monto
        print(f"Deposito aceptado. Nuevo saldo: ${self.saldo:,.2f}")

    def retirar(self, monto):
        if monto <= 0:
            print("Monto invalido: debe ser mayor a cero.")
            return
        if monto > self.saldo:
            print(f"Fondos insuficientes. Disponible: ${self.saldo:,.2f}")
            return
        self.saldo -= monto
        print(f"Retiro exitoso. Saldo restante: ${self.saldo:,.2f}")

    def ver_saldo(self):
        # :,.2f -> separador de miles y dos cifras decimales
        print(f"Cuenta de {self.titular}: ${self.saldo:,.2f}")


# prueba
mi_cuenta = CuentaBancaria("Carlos Ruiz")
mi_cuenta.depositar(300_000)
mi_cuenta.depositar(-50)      # falla: monto negativo
mi_cuenta.retirar(80_000)
mi_cuenta.retirar(500_000)   # falla: fondos insuficientes
mi_cuenta.ver_saldo()         # $220,000.00