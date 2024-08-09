class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.comprobador = True
        self.niveles = 0

    def insert(self, key):
        self.root = self._insertRecursively(self.root, key)

    def _insertRecursively(self, root, key):
        self.niveles+=1
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insertRecursively(root.left, key)
        elif key > root.key:
            root.right = self._insertRecursively(root.right, key)
        return root

    def search(self, key):
        if self._searchRecursively(self.root, key) != None:
            return True
        else:
            return False

    def _searchRecursively(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._searchRecursively(root.left, key)
        return self._searchRecursively(root.right, key)

    def delete(self, key):
        self.root = self._deleteRecursively(self.root, key)

    def _deleteRecursively(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._deleteRecursively(root.left, key)
        elif key > root.key:
            root.right = self._deleteRecursively(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = self._minValueNode(root.right).key
            root.right = self._deleteRecursively(root.right, root.key)
        return root

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inOrder(self):
        self._inOrderRecursively(self.root)
        return self.comprobador

    def _inOrderRecursively(self, root, elements):
        if root:
            self._inOrderRecursively(root.left, elements)
            if (root.left != None and root.right == None) or (root.left == None and root.right != None): self.comprobador = False
            self._inOrderRecursively(root.right, elements)
            

            
for _ in range(int(input())):
    arbol = BinarySearchTree()
    a = list(map(int,input().split()))[:-1:]
    c = 0
    niveles = 0
    for i in a:
        c+=1
        arbol.insert(i)
        if arbol.niveles>niveles: niveles = arbol.niveles
        arbol.niveles=0
    
    if (2**niveles)-1 == c:
        print("completo")
    else: print("no")
    