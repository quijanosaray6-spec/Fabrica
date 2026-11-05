class Objeto:
    def init(self, nombre, codigo, estado, ubicacion, material):
        self.nombre = nombre
        self.codigo = codigo
        self.estado = estado
        self.ubicacion = ubicacion
        self.material = material

    def mostrarInfo(self):
        print("Nombre:", self.nombre)
        print("Codigo:", self.codigo)
        print("Estado:", self.estado)
        print("Ubicacion:", self.ubicacion)
        print("Material:", self.material)

    def encender(self):
        self.estado = "Encendido"
        print("Objeto encendido")

    def apagar(self):
        self.estado = "Apagado"
        print("Objeto apagado")

    def cambiar_estado(self, estado):
        self.estado = estado

    def cambiar_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion
    
    def describir(self):
        print("Este objeto es:", self.nombre)
