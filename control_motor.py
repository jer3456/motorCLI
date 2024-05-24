class Motor:
    def __init__(self):
        self.encendido = False
        self.velocidad = 0

    def encender(self):
        if not self.encendido:
            self.encendido = True
            self.velocidad = 0
            print("Motor encendido.")
        else:
            print("El motor ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad = 0
            print("Motor apagado.")
        else:
            print("El motor ya está apagado.")

    def ajustar_velocidad(self, nueva_velocidad):
        if self.encendido:
            if 0 <= nueva_velocidad <= 100:
                self.velocidad = nueva_velocidad
                print(f"Velocidad ajustada a {nueva_velocidad}.")
            else:
                print("La velocidad debe estar entre 0 y 100.")
        else:
            print("No se puede ajustar la velocidad porque el motor está apagado.")

    def mostrar_estado(self):
        estado = "encendido" si self.encendido else "apagad
