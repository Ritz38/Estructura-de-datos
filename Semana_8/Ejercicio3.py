from collections import deque

class Nodo:
    def __init__(self, clave):
        self.clave = clave
        self.izq = None
        self.der = None
        self.altura = 1

class ArbolAVL:
    def __init__(self):
        self.raiz = None
        self.tamano = 0
        self.huella = []

    def insertar(self, clave):
        if not self.buscar(clave):
            self.raiz = self._insertar_recursivo(self.raiz, clave)

    def _insertar_recursivo(self, nodo, clave):
        if not nodo:
            nuevo_nodo = Nodo(clave)
            self.tamano += 1
            return nuevo_nodo
        elif clave < nodo.clave:
            nodo.izq = self._insertar_recursivo(nodo.izq, clave)
        else:
            nodo.der = self._insertar_recursivo(nodo.der, clave)

        nodo.altura = 1 + max(self._obtener_altura(nodo.izq), self._obtener_altura(nodo.der))
        balance = self._obtener_balance(nodo)

        if balance > 1:
            if clave < nodo.izq.clave:
                return self._rotar_derecha(nodo)
            else:
                nodo.izq = self._rotar_izquierda(nodo.izq)
                return self._rotar_derecha(nodo)

        if balance < -1:
            if clave > nodo.der.clave:
                return self._rotar_izquierda(nodo)
            else:
                nodo.der = self._rotar_derecha(nodo.der)
                return self._rotar_izquierda(nodo)

        return nodo

    def _rotar_izquierda(self, z):
        y = z.der
        temporal = y.izq
        y.izq = z
        z.der = temporal

        z.altura = 1 + max(self._obtener_altura(z.izq), self._obtener_altura(z.der))
        y.altura = 1 + max(self._obtener_altura(y.izq), self._obtener_altura(y.der))

        return y

    def _rotar_derecha(self, z):
        y = z.izq
        temporal = y.der
        y.der = z
        z.izq = temporal

        z.altura = 1 + max(self._obtener_altura(z.izq), self._obtener_altura(z.der))
        y.altura = 1 + max(self._obtener_altura(y.izq), self._obtener_altura(y.der))

        return y

    def _obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def _obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self._obtener_altura(nodo.izq) - self._obtener_altura(nodo.der)

    def buscar(self, clave):
        return self._buscar_recursivo(self.raiz, clave) is not None

    def _buscar_recursivo(self, nodo, clave):
        if nodo is None or nodo.clave == clave:
            return nodo
        if clave < nodo.clave:
            return self._buscar_recursivo(nodo.izq, clave)
        else:
            return self._buscar_recursivo(nodo.der, clave)

    def recorrido_por_niveles(self):
        resultado = []
        if not self.raiz:
            return resultado

        cola = deque([self.raiz])
        while cola:
            actual = cola.popleft()
            resultado.append(actual.clave)
            if not actual.izq and not actual.der:
                self.huella.append("0")
            elif not actual.izq:
                self.huella.append("1")
            elif not actual.der:
                self.huella.append("-1")
            else:
                self.huella.append("2")
            if actual.izq:
                cola.append(actual.izq)
            if actual.der:
                cola.append(actual.der)
        return resultado

while True:
    num_elementos = int(input())
    if num_elementos == 0:
        break
    arbol_avl = ArbolAVL()
    valores = map(int,input().split())
    for valor in valores:
        arbol_avl.insertar(valor)
    arbol_avl.recorrido_por_niveles()
    print(".".join(arbol_avl.huella))
