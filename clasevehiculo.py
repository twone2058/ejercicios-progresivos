class Vehiculo:

    def __init__(self, marca, modelo):
        self.marca     = marca
        self.modelo    = modelo
        self.velocidad = 0       # siempre arranca en reposo
        self.encendido = False  # siempre arranca apagado

    def encender(self):
        if self.encendido:
            print("El vehiculo ya esta en marcha.")
            return
        self.encendido = True
        print(f"{self.marca} encendido.")

    def acelerar(self, km):
        if not self.encendido:
            print("Primero enciende el vehiculo.")
            return
        self.velocidad += km
        print(f"Velocidad: {self.velocidad} km/h")

    def frenar(self, km):
        # max(0, ...) impide que la velocidad quede negativa
        self.velocidad = max(0, self.velocidad - km)
        print(f"Velocidad: {self.velocidad} km/h")

    def apagar(self):
        if self.velocidad > 0:
            print(f"Frena antes de apagar. Velocidad: {self.velocidad} km/h")
            return
        self.encendido = False
        print("Vehiculo apagado.")

    def estado(self):
        motor = "encendido" if self.encendido else "apagado"
        print(f"{self.marca} {self.modelo} | {self.velocidad} km/h | motor {motor}")


# prueba
auto = Vehiculo("Toyota", "Corolla")
auto.acelerar(30)    # falla: motor apagado
auto.encender()
auto.acelerar(80)
auto.apagar()        # falla: aun se mueve
auto.frenar(80)
auto.apagar()
auto.estado()