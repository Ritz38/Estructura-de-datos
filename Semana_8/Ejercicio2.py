from collections import deque

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.altura = 1

class ArbolAVL:
    def __init__(self):
        self.raiz = None
        self.tamano = 0
        self.factor_altura = 0

    def insertar(self, valor):
        if not self.buscar(valor):
            self.raiz = self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if not nodo:
            nuevo_nodo = Nodo(valor)
            self.tamano += 1
            return nuevo_nodo
        elif valor < nodo.valor:
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, valor)
        else:
            nodo.derecho = self._insertar_recursivo(nodo.derecho, valor)

        nodo.altura = 1 + max(self._obtener_altura(nodo.izquierdo), self._obtener_altura(nodo.derecho))
        balance = self._obtener_balance(nodo)

        if balance > 1:
            if valor < nodo.izquierdo.valor:
                return self._rotacion_derecha(nodo)
            else:
                nodo.izquierdo = self._rotacion_izquierda(nodo.izquierdo)
                return self._rotacion_derecha(nodo)

        if balance < -1:
            if valor > nodo.derecho.valor:
                return self._rotacion_izquierda(nodo)
            else:
                nodo.derecho = self._rotacion_derecha(nodo.derecho)
                return self._rotacion_izquierda(nodo)

        return nodo

    def _rotacion_izquierda(self, z):
        y = z.derecho
        temp = y.izquierdo
        y.izquierdo = z
        z.derecho = temp

        z.altura = 1 + max(self._obtener_altura(z.izquierdo), self._obtener_altura(z.derecho))
        y.altura = 1 + max(self._obtener_altura(y.izquierdo), self._obtener_altura(y.derecho))

        return y

    def _rotacion_derecha(self, z):
        
        
        y = z.izquierdo
        temp = y.derecho
        y.derecho = z
        z.izquierdo = temp

        z.altura = 1 + max(self._obtener_altura(z.izquierdo), self._obtener_altura(z.derecho))
        y.altura = 1 + max(self._obtener_altura(y.izquierdo), self._obtener_altura(y.derecho))



        return y

    def _obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura
    
    
    

    def _obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self._obtener_altura(nodo.izquierdo) - self._obtener_altura(nodo.derecho)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor) is not None

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo
        if valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierdo, valor)
        else:
            return self._buscar_recursivo(nodo.derecho, valor)

    def recorrido_por_niveles(self):
        resultado = []
        if not self.raiz:
            return resultado

        cola = deque([self.raiz])
        while cola:
            actual = cola.popleft()
            if actual.izquierdo is None and actual.derecho is None:
                resultado.append(actual.valor)
            if actual.izquierdo and actual.izquierdo.altura == actual.altura - 1:
                cola.append(actual.izquierdo)
            if actual.derecho and actual.derecho.altura == actual.altura - 1:
                cola.append(actual.derecho)
                
                
        return len(resultado)
    

for _ in range(int(input())):
    entradas = map(int,input().split()[:-1])
    arbol_avl = ArbolAVL()
    for numero in entradas:
        arbol_avl.insertar(numero)
    print(arbol_avl.recorrido_por_niveles())
