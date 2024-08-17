class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insertRecursively(self.root, key)

    def _insertRecursively(self, root, key):
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
        elements = []
        self._inOrderRecursively(self.root, elements)
        return elements

    def _inOrderRecursively(self, root, elements):
        if root:
            elements.append(root.key)
            self._inOrderRecursively(root.left, elements)
            self._inOrderRecursively(root.right, elements)



for _ in range(int(input())):
    a = BinarySearchTree()
    l = list(map(int,input().split()))
    l = l[:-1:]
    for i in l:
        a.insert(i)
    r=""
    for j in a.inOrder():
        r+=str(j)
    print(r)
    
    