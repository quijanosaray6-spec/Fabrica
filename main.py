from Objeto import Objeto 
from Maquina import Maquina
from Empleado import Empleado
from Carro import Carro

def main():
    objeto1 = Objeto(
        "Herramienta", "O01", "Activo", "Taller", "Metal"
    )

    maquina1 = Maquina(
        "Brazo robotico", "M01", "Encendido", "Fabrica", "Metal", "Robor industrial", 2000, 50, 100, True
    )

    empleado1 = Empleado(
        "Carlos", "E01", "Activo", "Fabrica", "Humano", "12345", "Supervisor", "Manana", 5, True
    )

    carro1 = Carro(
        "Automovil", "C01", "En fabricacion", "Fabrica", "Metal", "Toyota", "Blanco", 2026, 0, False
    )

    print("Objeto")
    objeto1.mostrar_info()
    objeto1.describir()

    print()
    print("Maquina")
    maquina1.mostrar_info()
    maquina1.iniciar_trabajo()
    maquina1.revisar_capacidad()

    print()
    print("Empleado")
    empleado1.mostrar_info()
    empleado1.mostrar_empleado()
    empleado1.supervisar_maquina()

    print()
    print("Carro")
    carro1.mostrar_info()
    carro1.mostrar_carro()
    carro1.arrancar()
    carro1.finalizar_fabricacion()

    if __name__ == "__main__":
        main()