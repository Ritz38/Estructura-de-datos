class Nodo(object):
    def __init__(self, clave):
        self.clave = clave
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class ArbolAVL(object):
    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def insertar(self, clave):
        if not self.buscar(clave):
            self.raiz = self._insertarRecursivo(self.raiz, clave)

    def _insertarRecursivo(self, raiz, clave):
        if not raiz:
            nodo_nuevo = Nodo(clave)
            self.tamano += 1
            return nodo_nuevo
        elif clave < raiz.clave:
            raiz.izquierda = self._insertarRecursivo(raiz.izquierda, clave)
        else:
            raiz.derecha = self._insertarRecursivo(raiz.derecha, clave)

        raiz.altura = 1 + max(self._obtenerAltura(raiz.izquierda), self._obtenerAltura(raiz.derecha))

        factorBalance = self._obtenerBalance(raiz)

        if factorBalance > 1:
            if clave < raiz.izquierda.clave:
                return self._rotarDerecha(raiz)
            else:
                raiz.izquierda = self._rotarIzquierda(raiz.izquierda)
                return self._rotarDerecha(raiz)

        if factorBalance < -1:
            if clave > raiz.derecha.clave:
                return self._rotarIzquierda(raiz)
            else:
                raiz.derecha = self._rotarDerecha(raiz.derecha)
                return self._rotarIzquierda(raiz)

        return raiz

    def _rotarIzquierda(self, z):
        y = z.derecha
        auxiliar = y.izquierda
        y.izquierda = z
        z.derecha = auxiliar
        z.altura = 1 + max(self._obtenerAltura(z.izquierda), self._obtenerAltura(z.derecha))
        y.altura = 1 + max(self._obtenerAltura(y.izquierda), self._obtenerAltura(y.derecha))
        return y

    def _rotarDerecha(self, z):
        y = z.izquierda
        auxiliar = y.derecha
        y.derecha = z
        z.izquierda = auxiliar
        z.altura = 1 + max(self._obtenerAltura(z.izquierda), self._obtenerAltura(z.derecha))
        y.altura = 1 + max(self._obtenerAltura(y.izquierda), self._obtenerAltura(y.derecha))
        return y

    def _obtenerAltura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def _obtenerBalance(self, nodo):
        if not nodo:
            return 0
        return self._obtenerAltura(nodo.izquierda) - self._obtenerAltura(nodo.derecha)

    def buscar(self, clave):
        return self._buscarRecursivo(self.raiz, clave) is not None

    def _buscarRecursivo(self, raiz, clave):
        if raiz is None or raiz.clave == clave:
            return raiz
        if clave < raiz.clave:
            return self._buscarRecursivo(raiz.izquierda, clave)
        else:
            return self._buscarRecursivo(raiz.derecha, clave)

    def recorridoPostOrden(self):
        elementos = []
        self._recorridoPostOrdenRecursivo(self.raiz, elementos)
        return elementos

    def _recorridoPostOrdenRecursivo(self, raiz, elementos):
        if raiz:
            self._recorridoPostOrdenRecursivo(raiz.izquierda, elementos)
            self._recorridoPostOrdenRecursivo(raiz.derecha, elementos)
            elementos.append(raiz.clave)

for i in range(int(input())):
    avl = ArbolAVL()
    entradas = input().split()[:-1]
    for clave in entradas:
        avl.insertar(clave)
    for clave in avl.recorridoPostOrden():
        print(clave, end="")
    print()
