
class SaaSManager:

    def __init__(self):
        self.empresas = {}

    def registrar_empresa(self, nombre):
        self.empresas[nombre] = {"empleados": []}

    def agregar_empleado(self, empresa, empleado):
        self.empresas[empresa]["empleados"].append(empleado)
