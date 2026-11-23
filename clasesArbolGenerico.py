class Alumno:
    def __init__(self, matricula, nombre, promedio):
        self.matricula = matricula
        self.nombre = nombre
        self.promedio = promedio

    def __str__(self):
        return (
            f"Matricula: {self.matricula}, "
            f"Nombre: {self.nombre}, "
            f"Promedio: {self.promedio}"
        )

class Incidente:
    def __init__(self, idIncidente, direccionIP, tipoAtaque, nivelRiesgo, estado):
        self.idIncidente = idIncidente
        self.direccionIP = direccionIP
        self.tipoAtaque = tipoAtaque
        self.nivelRiesgo = nivelRiesgo
        self.estado = estado
    
    def __str__(self):
        return (
            f"ID: {self.idIncidente}, "
            f"IP: {self.direccionIP}, "
            f"Tipo de Incidente: {self.tipoIncidente}, "
            f"Nivel de riesgo: {self.nivelRiesgo}, "
            f"Estado: {self.estado}"
        )

class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return (
            f"Codigo: {self.codigo}, "
            f"Nombre: {self.nombre}, "
            f"Precio: {self.precio}"
        )