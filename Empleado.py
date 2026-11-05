from Objeto import Objeto

class Empleado(Objeto):
    def __init__(self, nombre, codigo, estado, ubicacion, material, documento, cargo, turno, experiencia, trabajando):
        super().__init__(nombre, codigo, estado, ubicacion, material)
        self.documento = documento
        self.cargo = cargo
        self.turno = turno
        self.experiencia = experiencia
        self.trabajando = trabajando

    def mostrar_empleado(self):
        print("Documento:", slef.documento)
        print("Cargo:", self.cargo)

    def iniciar_turno(self):
        self.trabajando = True
        print("Turno terminado")

    def supervisar_maquina(self):
        print("Supervisando la maquina")

    def revisar_carro(self):
        print("Revisando el carro")

    def reportar_problema(self):
        print("Problema reportado")
