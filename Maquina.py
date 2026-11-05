from Objeto import Objeto 

class Maquina(Objeto):
    def __init__(self, nombre, codigo, estado, ubicacion, material, tipo, potencia, velocidad, capacidad, operatividad):
        super().__init__(nombre, codigo, estado, ubicacion, material)
        self.tipo = tipo
        self.potencia = potencia
        self.velocidad = velocidad
        self.capacidad = capacidad
        self.operatividad = operatividad

    def mostrar_maquina(self):
        print("Tipo:", self.tipo)
        print("Potencia:", self.potencia)

    def iniciar_trabajo(self):
        self.operatividad = True
        print("Maquina trabajando")

    def detener_trabajo(self):
        self.operatividad = False
        print("Maquina detenida")

    def ajustar_velocidad(self, velocidad):
        self.velocidad = velocidad

    def revisar_capacidad(self):
        print("Capacidad:", self.capacidad)

    def realizar_mantenimiento(self):
        print("Mantenimiento realizado")
