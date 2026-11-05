from Objeto import Objeto 

class Carro(Objeto):
    def __init__(self, nombre, codigo, estado, ubicacion, material, marca, color, modelo, velocidad, terminado):
        super().__init__(nombre, codigo, estado, ubicacion, material)
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.velocidad = velocidad
        self.terminado = terminado

    def mostrar_carro(self):
        print("Marca:", self.marca)
        print("Color:", self.color)
        print("Modelo:", self.modelo)

    def arrancar(self):
        self.estado = "En movimiento"
        print("Carro arrancando")

    def detener(self):
        self.estado = "Detenido"
        print("Carro detenido")

    def cambiar_color(self, color):
        self.color = color

    def revisar_velocidad(self):
        print("Velocidad:", self.velocidad)

    def finalizar_fabricacion(self):
        self.terminado = True
        print("Fabricacion terminada")
