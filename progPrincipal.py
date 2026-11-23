from arbolBinarioGeerico import ArbolBinario
from clasesArbolGenerico import Alumno, Incidente, Producto

### ALUMNOS
arbolAlumno = ArbolBinario(clave=lambda alumno: alumno.matricula)
a1 = Alumno(20, "Hector", 85)
arbolAlumno.insertarNodo(a1)

a2 = Alumno(10, "Saul", 80)
arbolAlumno.insertarNodo(a2)

a3 = Alumno(30, "Alejandro", 82)
arbolAlumno.insertarNodo(a3)

a4 = Alumno(50, "Juliana", 90)
arbolAlumno.insertarNodo(a4)

a5 = Alumno(40, "Rosa", 78)
arbolAlumno.insertarNodo(a5)

arbolAlumno.imprimirArbol()

arbolAlumno.inOrden()
arbolAlumno.preOrden()
arbolAlumno.posOrden()

alumnoBuscar = Alumno(30, "", "")
print(arbolAlumno.buscarNodo(alumnoBuscar))
print("")
alumnoBuscar = Alumno(70, "", "")
print(arbolAlumno.buscarNodo(alumnoBuscar))
print("")

print(arbolAlumno.contarNodos())
print("")
    
print(arbolAlumno.obtenerMayor())
print(arbolAlumno.obtenerMenor())

print("\nINTRODUCOR OTRO ALUMNO CON MATRICULA 40.")
numMatricula = int(input("Matricula: "))
nombre = input("Nombre: ")
prom = input("Promedio: ")
alumnoNuevo = Alumno(numMatricula, nombre, prom)

if arbolAlumno.buscarNodo(alumnoNuevo):
    print(f"ERROR: Ya existe un alumno con matricula: {alumnoNuevo.matricula}")
else:
    arbolAlumno.insertarNodo(alumnoNuevo)

### INCIDENTES
arbolIncidente = ArbolBinario(clave=lambda incidente: incidente.idIncidente)
inc1 = Incidente(150, "192.168.1.25", "Fuerza bruta", "ALTO", "Resuelto")
arbolIncidente.insertarNodo(inc1)

inc2 = Incidente(100, "192.168.1.30", "Malware", "CRITICO", "Resuelto")
arbolIncidente.insertarNodo(inc2)

inc3 = Incidente(200, "10.0.0.15", "Escaneo de puertos", "MEDIO", "Resuelto")
arbolIncidente.insertarNodo(inc3)

inc4 = Incidente(75, "192.168.1.45", "Phishing", "ALTO", "Pendiente")
arbolIncidente.insertarNodo(inc4)

inc5 = Incidente(125, "10.0.0.20", "Acceso no autorizado", "CRITICO", "Pendiente")
arbolIncidente.insertarNodo(inc5)

inc6 = Incidente(175, "192.168.1.80", "Ransomware", "CRITICO", "En investigacion")
arbolIncidente.insertarNodo(inc6)

inc7 = Incidente(250, "10.0.0.50", "Denegacion de servicio", "ALTO", "En investigacion")
arbolIncidente.insertarNodo(inc7)

arbolIncidente.imprimirArbol()

arbolIncidente.inOrden()
arbolIncidente.preOrden()
arbolIncidente.posOrden()

incidenteBuscar = Incidente(125, "", "", "", "")
print(arbolIncidente.buscarNodo(incidenteBuscar))
print("")
incidenteBuscar = Incidente(300, "", "", "", "")
print(arbolIncidente.buscarNodo(incidenteBuscar))
print("")

print(arbolIncidente.contarNodos())
print("")
    
print(arbolIncidente.obtenerMayor())
print(arbolIncidente.obtenerMenor())

print("\nINTRODUCOR OTRO INCIDENTE CON ID 150.")
idInc = int(input("ID: "))
ip = input("IP: ")
tipoIncidente = input("Tipo de incidente: ")
nivRiesgo = input("Nivel de riesgo: ").upper()
est = input("Estado: ")
incNuevo = Incidente(idInc, ip, tipoIncidente, nivRiesgo, est)

if arbolIncidente.buscarNodo(incNuevo):
    print(f"ERROR: Ya existe un incidente con ID: {incNuevo.idIncidente}")
else:
    arbolIncidente.insertarNodo(incNuevo)

### PRODUCTOS
arbolProducto = ArbolBinario(clave=lambda producto: producto.codigo)
p1 = Producto(450, "Papel", 85)
arbolProducto.insertarNodo(p1)

p2 = Producto(230, "Jabon", 80)
arbolProducto.insertarNodo(p2)

p3 = Producto(250, "Papas", 82)
arbolProducto.insertarNodo(p3)

p4 = Producto(760, "Platanos", 90)
arbolProducto.insertarNodo(p4)

p5 = Producto(430, "Camisa", 78)
arbolProducto.insertarNodo(p5)

arbolProducto.imprimirArbol()

arbolProducto.inOrden()
arbolProducto.preOrden()
arbolProducto.posOrden()

productoBuscar = Producto(760, "", "")
print(arbolProducto.buscarNodo(productoBuscar))
print("")
productoBuscar = Producto(870, "", "")
print(arbolProducto.buscarNodo(productoBuscar))
print("")

print(arbolProducto.contarNodos())
print("")
    
print(arbolProducto.obtenerMayor())
print(arbolProducto.obtenerMenor())

print("\nINTRODUCOR OTRO PRODUCTO CON CODIGO 230.")
codigoProd = int(input("Codigo: "))
nombreProd = input("Nombre: ")
precioProd = input("Precio: ")
productoNuevo = Producto(codigoProd, nombreProd, precioProd)

if arbolProducto.buscarNodo(productoNuevo):
    print(f"ERROR: Ya existe un producto con matricula: {productoNuevo.codigo}")
else:
    arbolProducto.insertarNodo(productoNuevo)