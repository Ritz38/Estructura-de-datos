from collections import deque

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class ArbolAVL:
    def __init__(self):
        self.tamano = 0
        self.raiz = None
        self.subarbol = 1

    def insertar(self, valor):
        if not self.buscar(valor):
            self.raiz = self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if not nodo:
            nuevo_nodo = Nodo(valor)
            self.tamano += 1
            return nuevo_nodo
        elif valor < nodo.valor:
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, valor)
        else:
            nodo.derecha = self._insertar_recursivo(nodo.derecha, valor)

        nodo.altura = 1 + max(self._obtener_altura(nodo.izquierda),
                              self._obtener_altura(nodo.derecha))

        factor_balance = self._calcular_balance(nodo)
        if factor_balance > 1:
            if valor < nodo.izquierda.valor:
                return self._rotar_derecha(nodo)
            else:
                nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
                return self._rotar_derecha(nodo)

        if factor_balance < -1:
            if valor > nodo.derecha.valor:
                return self._rotar_izquierda(nodo)
            else:
                nodo.derecha = self._rotar_derecha(nodo.derecha)
                return self._rotar_izquierda(nodo)

        return nodo

    def _rotar_izquierda(self, z):
        y = z.derecha
        t2 = y.izquierda
        y.izquierda = z
        z.derecha = t2
        z.altura = 1 + max(self._obtener_altura(z.izquierda), self._obtener_altura(z.derecha))
        y.altura = 1 + max(self._obtener_altura(y.izquierda), self._obtener_altura(y.derecha))
        return y

    def _rotar_derecha(self, z):
        y = z.izquierda
        t3 = y.derecha
        y.derecha = z
        z.izquierda = t3
        z.altura = 1 + max(self._obtener_altura(z.izquierda), self._obtener_altura(z.derecha))
        y.altura = 1 + max(self._obtener_altura(y.izquierda), self._obtener_altura(y.derecha))
        return y

    def _obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def _calcular_balance(self, nodo):
        if not nodo:
            return 0
        return self._obtener_altura(nodo.izquierda) - self._obtener_altura(nodo.derecha)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor) is not None

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo
        if valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo.derecha, valor)

    def contar_nodos(self, nodo):
        if not nodo:
            return 0
        return 1 + self.contar_nodos(nodo.izquierda) + self.contar_nodos(nodo.derecha)

    def obtener_subarbol_max(self):
        self._recorrer_inorden(self.raiz)
        return self.subarbol

    def _recorrer_inorden(self, nodo):
        if nodo:
            if nodo.derecha is None or nodo.izquierda is None:
                pass
            elif (nodo.altura > self.subarbol) and (((2 ** nodo.altura) - 1) == self.contar_nodos(nodo)):
                self.subarbol = nodo.altura
            self._recorrer_inorden(nodo.izquierda)
            self._recorrer_inorden(nodo.derecha)

while True:
    cantidad = int(input())
    if cantidad == 0:
        break
    arbol = ArbolAVL()
    elementos = list(map(int, input().split()))
    for elemento in elementos:
        arbol.insertar(elemento)

    print(arbol.obtener_subarbol_max())
