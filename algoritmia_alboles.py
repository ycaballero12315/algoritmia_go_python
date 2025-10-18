class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return f'El Nodo es {Node}'
    
class TreeBST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            
        self._recursive_insert(self.root, value)

    def _recursive_insert(self, current_node:Node, value):
        if value< current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._recursive_insert(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._recursive_insert(current_node.right, value)
        else:
            return f"El valor: {value} ya existe en el arbol"
    
    def search_node(self, value)->bool:

        return self._recursive_search_node(self.root,value)
    
    def _recursive_search_node(self, current_node, value):
        if current_node is None:
            return False
        
        if current_node.value == value:
            return True
        
        if value < current_node.value:
            return self._recursive_search_node(current_node.left, value)

        else:
            return self._recursive_search_node(current_node.right, value)
    
    def inorder(self)->list:
        # '''Este metodo guarda en 
        #   /una lista de forma ordenada los elementos 
        #   /de menor a mayos, desde el nodo mas quequenno
        #   / que es el mas inferior izquierdo'''
        
        result: list= []
        self._recursive_inorder(self.root, result)
        return result
    
    def _recursive_inorder(self, node:Node, result:list):
        if node:
            self._recursive_inorder(node.left, result)
            result.append(node.value)
            self._recursive_inorder(node.right, result)
    
    def preorder(self)->list:
        '''Guarda Padre->Hijo izquierdo-> Hijo Derecho'''
        
        result: list= []
        self._recursive_preorder(self.root, result)
        return result
    
    def _recursive_preorder(self, node:Node, result:list):
        if node:
            result.append(node.value)
            self._recursive_inorder(node.left, result)
            self._recursive_inorder(node.right, result)
    
    def postorder(self)->list:
        '''Guarda Hijo izquierdo-> Hijo Derecho-> Padre->'''
        
        result: list= []
        self._recursive_postorder(self.root, result)
        return result
    
    def _recursive_postorder(self, node:Node, result:list):
        if node:
            result.append(node.value)
            self._recursive_inorder(node.left, result)
            self._recursive_inorder(node.right, result)

    def find_min(self):
        current = self.root

        if current is None:
            return None
        
        while current.left:
            current = current.left
        
        return current
    
    def find_max(self):
        current = self.root
        if current is None:
            return None
        
        while current.right:
            current = current.right
        
        return current
    
    def tree_height(self):

        height = self._recursive_height(self.root)
        return height

    def _recursive_height(self, node:Node):
        if node is None:
            return -1
        
        left_height = self._recursive_height(node.left)
        right_height = self._recursive_height(node.right)

        return 1 + max(left_height, right_height)
    
    def count_nodes(self)->int:
        
        count = self._recursive_count(self.root)
        return count

    def _recursive_count(self, node:Node):
        if node is None:
            return 0
        
        return 1 + self._recursive_count(node.left) + self._recursive_count(node.right)
    
    def count_hojas(self):

        count = self._count_hojas_recursive(self.root)
        return count

    def _count_hojas_recursive(self, node:Node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        
        return self._count_hojas_recursive(node.left) + self._count_hojas_recursive(node.right)
    
    def visualize(self):
        """
        Muestra el árbol de forma visual (básica).
        """
        print("\n" + "="*60)
        print("Arbol")
        print("="*60)
        self._visualize_recursive(self.root, "", True)
        print("="*60)
    
    def _visualize_recursive(self, node:Node, prefix, is_tail):
        if node is not None:
            print(prefix + ("└── " if is_tail else "├── ") + str(node.value))
            
            # Preparar el prefijo para los hijos
            children = [node.left, node.right]
            for i, child in enumerate(children):
                if child is not None:
                    extension = "    " if is_tail else "│   "
                    self._visualize_recursive(child, prefix + extension, i == len(children) - 1)

if __name__ == "__main__":
    print("="*60)
    print("BINARY SEARCH TREE - DEMOSTRACIÓN COMPLETA")
    print("="*60)
    
    bst = TreeBST()
    
    print("\n" + "─"*60)
    print("FASE 1: CONSTRUCCIÓN DEL ÁRBOL")
    print("─"*60)
    
    valores = [50, 30, 70, 20, 40, 60, 80]
    print(f"Insertaremos: {valores}")
    
    for valor in valores:
        bst.insert(valor)
    
    # Visualizar
    bst.visualize()
    
    # Buscar elementos
    print("\n" + "─"*60)
    print("FASE 2: BÚSQUEDAS")
    print(bst.search_node(40))
    print("─"*60)
    
    bst.search_node(40)  
    bst.search_node(100) 
    
    # Recorridos
    print("\n" + "─"*60)
    print("FASE 3: RECORRIDOS")
    print(f'inOrder: {bst.inorder() }')
    print("─"*60)
    
    bst.inorder()   
    bst.preorder()   
    bst.postorder()  
    
    # Operaciones útiles
    print("\n" + "─"*60)
    print("FASE 4: OPERACIONES ÚTILES")
    print(f"Cantidad de hojas: {bst.count_hojas()}")
    print("─"*60)
    
    bst.find_min()      
    bst.find_max()      
    bst.tree_height()        
    bst.count_nodes()   
    bst.count_hojas()  
    
    print("\n" + "="*60)
    print("DEMOSTRACIÓN COMPLETADA")
    print("="*60)



        
        
    
