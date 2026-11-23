from arbolBinarioGeerico import ArbolBinario
from clasesArbolGenerico import Alumno

# Crear el arbol ordenado por matricula
arbol = ArbolBinario(clave=lambda alumno: alumno.matricula)

a1 = Alumno(105, "Ana", 90)
a2 = Alumno(102, "Luis", 85)
a3 = Alumno(108, "Carlos", 95)
a4 = Alumno(101, "Maria", 88)
a5 = Alumno(106, "Pedro", 92)
a6 = Alumno(103, "Sofia", 89)

arbol.insertarNodo(a1)
arbol.insertarNodo(a2)
arbol.insertarNodo(a3)
arbol.insertarNodo(a4)
arbol.insertarNodo(a5)
arbol.insertarNodo(a6)

# Imprimir arbol
print("ARBOL BINARIO:")
arbol.imprimirArbol()

# Recorridos
print("\nRECORRIDO INORDEN:")
arbol.inOrden()
print("\nRECORRIDO PREORDEN:")
arbol.preOrden()
print("\nRECORRIDO POSORDEN:")
arbol.posOrden()

# Buscar alumno por matricula
alumnoBuscar = Alumno(106, "", 0)
if arbol.buscarNodo(alumnoBuscar):
    print("\nEl alumno existe.")
else:
    print("\nEl alumno no existe")

# Eliminar alumno
arbol.eliminarNodo(Alumno(102, "", 0))

print("\nARBOL DESPUES DE ELIMINAR:")
arbol.imprimirArbol()