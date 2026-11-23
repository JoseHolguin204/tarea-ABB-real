class NodoArbol:
    def __init__(self, d):
        self.dato = d
        self.hijoIzquierdo = None
        self.hijoDerecho = None

    def __str__(self):
        return str(self.dato)


class ArbolBinario:
    def __init__(self, clave=None):
        self.raiz = None
        self.tam = 0
        self.clave = clave if clave is not None else (lambda x: x)

    def isEmpty(self):
        return self.raiz is None

    def insertarNodo(self, dato):
        self.raiz = self._insertar(self.raiz, dato)

    def _insertar(self, actual, dato):
        if actual is None:
            self.tam += 1
            return NodoArbol(dato)
        if self.clave(dato) < self.clave(actual.dato):
            actual.hijoIzquierdo = self._insertar(actual.hijoIzquierdo, dato)
        elif self.clave(dato) > self.clave(actual.dato):
            actual.hijoDerecho = self._insertar(actual.hijoDerecho, dato)

        # Si las claves son iguales, no se inserta.
        return actual

    def buscarNodo(self, dato):
        return self._buscar(self.raiz, self.clave(dato))

    def _buscar(self, actual, clave):
        if actual is None:
            return False
        if self.clave(actual.dato) == clave:
            return True

        if clave < self.clave(actual.dato):
            return self._buscar(actual.hijoIzquierdo, clave)
        else:
            return self._buscar(actual.hijoDerecho, clave)

    def obtenerMenor(self):
        if self.raiz is None:
            return None
        nodo = self._minimo(self.raiz)
        return self.clave(nodo.dato)

    def _minimo(self, actual):
        while actual.hijoIzquierdo is not None:
            actual = actual.hijoIzquierdo
        return actual

    def obtenerMayor(self):
        if self.raiz is None:
            return None
        nodo = self._maximo(self.raiz)
        return self.clave(nodo.dato)

    def _maximo(self, actual):
        while actual.hijoDerecho is not None:
            actual = actual.hijoDerecho
        return actual

    def eliminarNodo(self, dato):
        self.raiz = self._eliminar(self.raiz, self.clave(dato))

    def _eliminar(self, actual, clave):
        if actual is None:
            return None
        if clave < self.clave(actual.dato):
            actual.hijoIzquierdo = self._eliminar(actual.hijoIzquierdo, clave)
        elif clave > self.clave(actual.dato):
            actual.hijoDerecho = self._eliminar(actual.hijoDerecho, clave)
        else:
            # CASO 1: Nodo sin hijos
            if actual.hijoIzquierdo is None and actual.hijoDerecho is None:
                self.tam -= 1
                return None
            # CASO 2: Nodo con un solo hijo
            elif actual.hijoIzquierdo is None:
                self.tam -= 1
                return actual.hijoDerecho
            elif actual.hijoDerecho is None:
                self.tam -= 1
                return actual.hijoIzquierdo
            # CASO 3: Nodo con dos hijos
            else:
                sucesor = self._minimo(actual.hijoDerecho)
                actual.dato = sucesor.dato
                actual.hijoDerecho = self._eliminar(
                    actual.hijoDerecho, self.clave(sucesor.dato)
                )

        return actual

    def contarNodos(self):
        return self.tam

    def imprimirArbol(self):
        self._imprimir(self.raiz, 0)

    def _imprimir(self, actual, nivel):
        if actual is not None:
            self._imprimir(actual.hijoDerecho, nivel + 1)
            print("    " * nivel + str(self.clave(actual.dato)))
            self._imprimir(actual.hijoIzquierdo, nivel + 1)

    def inOrden(self):
        self._inOrden(self.raiz)
        print()

    def _inOrden(self, actual):
        if actual is not None:
            self._inOrden(actual.hijoIzquierdo)
            print(self.clave(actual.dato), end=" ")
            self._inOrden(actual.hijoDerecho)

    def preOrden(self):
        self._preOrden(self.raiz)
        print()

    def _preOrden(self, actual):
        if actual is not None:
            print(self.clave(actual.dato), end=" ")
            self._preOrden(actual.hijoIzquierdo)
            self._preOrden(actual.hijoDerecho)

    def posOrden(self):
        self._posOrden(self.raiz)
        print()

    def _posOrden(self, actual):
        if actual is not None:
            self._posOrden(actual.hijoIzquierdo)
            self._posOrden(actual.hijoDerecho)
            print(self.clave(actual.dato), end=" ")