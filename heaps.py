class HeapSort:
    """
    Implementación educativa de Heap Sort con visualización paso a paso.
    """
    
    def __init__(self):
        self.pasos = 0  # Contador de operaciones
    
    # ==================== OPERACIONES AUXILIARES ====================
    
    def get_parent(self, i):
        """
        Obtiene el índice del padre de un nodo.
        Fórmula: (i - 1) // 2
        
        Ejemplo: hijo en índice 4 → padre en (4-1)//2 = 1
        """
        return (i - 1) // 2
    
    def get_left_child(self, i):
        """
        Obtiene el índice del hijo izquierdo.
        Fórmula: 2 * i + 1
        
        Ejemplo: padre en índice 1 → hijo izq en 2*1+1 = 3
        """
        return 2 * i + 1
    
    def get_right_child(self, i):
        """
        Obtiene el índice del hijo derecho.
        Fórmula: 2 * i + 2
        
        Ejemplo: padre en índice 1 → hijo der en 2*1+2 = 4
        """
        return 2 * i + 2
    
    # ==================== VISUALIZACIÓN ====================
    
    def visualizar_array_como_arbol(self, arr, heap_size=None):
        """
        Muestra el array como un árbol binario.
        """
        if heap_size is None:
            heap_size = len(arr)
        
        print("\n   📊 Array:", arr[:heap_size], "| Ordenados:", arr[heap_size:])
        print("   🌳 Estructura de árbol:")
        
        if heap_size == 0:
            print("      (vacío)")
            return
        
        # Calcular niveles del árbol
        import math
        max_nivel = int(math.log2(heap_size)) + 1
        
        # Imprimir por niveles
        idx = 0
        for nivel in range(max_nivel):
            nodos_en_nivel = 2 ** nivel
            espacios = " " * (2 ** (max_nivel - nivel - 1) * 2)
            
            nivel_str = espacios
            for _ in range(nodos_en_nivel):
                if idx < heap_size:
                    nivel_str += f"{arr[idx]:3} " + espacios
                    idx += 1
                else:
                    break
            
            print(f"      {nivel_str}")
            if idx >= heap_size:
                break
    
    # ==================== HEAPIFY (HUNDIR) ====================
    
    def heapify(self, arr, n, i, verbose=True):
        """
        "Hunde" un nodo para mantener la propiedad de Max Heap.
        
        Proceso:
        1. Compara el nodo con sus hijos
        2. Si algún hijo es mayor, hace swap
        3. Repite recursivamente en el hijo swapeado
        
        Parámetros:
        - arr: el array
        - n: tamaño del heap (no del array completo)
        - i: índice del nodo a hundir
        """
        largest = i  # Asumimos que el padre es el mayor
        left = self.get_left_child(i)
        right = self.get_right_child(i)
        
        if verbose:
            print(f"\n   🔍 Heapify en índice {i} (valor={arr[i]})")
        
        # Verificar si el hijo izquierdo existe y es mayor
        if left < n and arr[left] > arr[largest]:
            largest = left
            if verbose:
                print(f"      ⬅️  Hijo izquierdo {arr[left]} > padre {arr[i]}")
        
        # Verificar si el hijo derecho existe y es mayor
        if right < n and arr[right] > arr[largest]:
            largest = right
            if verbose:
                print(f"      ➡️  Hijo derecho {arr[right]} > padre {arr[i]}")
        
        # Si el mayor no es el padre, hacer swap y hundir recursivamente
        if largest != i:
            if verbose:
                print(f"      🔄 SWAP: {arr[i]} ↔ {arr[largest]}")
            
            arr[i], arr[largest] = arr[largest], arr[i]
            self.pasos += 1
            
            # Hundir recursivamente el nodo afectado
            self.heapify(arr, n, largest, verbose)
        else:
            if verbose:
                print(f"      ✅ Nodo {arr[i]} ya está en posición correcta")
    
    # ==================== CONSTRUIR HEAP ====================
    
    def build_max_heap(self, arr, verbose=True):
        """
        Convierte un array desordenado en un Max Heap.
        
        Estrategia:
        - Empezamos desde el último nodo NO-HOJA
        - Aplicamos heapify a cada nodo hacia arriba
        
        ¿Por qué desde el último no-hoja?
        Las hojas ya son heaps válidos (no tienen hijos).
        
        Complejidad: O(n)
        """
        n = len(arr)
        
        if verbose:
            print("\n" + "="*70)
            print("🏗️  FASE 1: CONSTRUIR MAX HEAP")
            print("="*70)
            print(f"Array inicial: {arr}")
        
        # El último nodo no-hoja está en n//2 - 1
        start_idx = n // 2 - 1
        
        if verbose:
            print(f"\nComenzamos desde índice {start_idx} (último padre)")
            print("Aplicamos heapify hacia arriba hasta el root...")
        
        # Aplicar heapify desde el último padre hasta el root
        for i in range(start_idx, -1, -1):
            if verbose:
                print(f"\n--- Procesando índice {i} ---")
            self.heapify(arr, n, i, verbose)
            if verbose:
                self.visualizar_array_como_arbol(arr)
        
        if verbose:
            print("\n✅ Max Heap construido!")
            self.visualizar_array_como_arbol(arr)
    
    # ==================== HEAP SORT ====================
    
    def heap_sort(self, arr, verbose=True):
        """
        Ordena un array usando Heap Sort.
        
        Algoritmo:
        1. Construir Max Heap
        2. Repetir n veces:
           a. Swap root (mayor) con último elemento
           b. Reducir tamaño del heap
           c. Heapify el nuevo root
        
        Complejidad: O(n log n)
        """
        self.pasos = 0
        n = len(arr)
        
        if verbose:
            print("\n" + "="*70)
            print("🎯 HEAP SORT - ALGORITMO COMPLETO")
            print("="*70)
            print(f"Array original: {arr}")
        
        # FASE 1: Construir Max Heap
        self.build_max_heap(arr, verbose)
        
        # FASE 2: Extraer elementos uno por uno
        if verbose:
            print("\n" + "="*70)
            print("📤 FASE 2: EXTRAER ELEMENTOS (ORDENAR)")
            print("="*70)
        
        # Extraer desde el final hacia el inicio
        for i in range(n - 1, 0, -1):
            if verbose:
                print(f"\n--- Iteración {n - i} ---")
                print(f"   🔄 SWAP: root {arr[0]} ↔ último elemento {arr[i]}")
            
            # Swap: poner el mayor (root) al final
            arr[0], arr[i] = arr[i], arr[0]
            self.pasos += 1
            
            if verbose:
                print(f"   📊 Array después del swap: {arr}")
                print(f"   🔒 Elemento {arr[i]} ahora está en su posición final")
                print(f"   📏 Nuevo tamaño del heap: {i}")
            
            # Heapify el nuevo root (con heap reducido)
            if verbose:
                print(f"   🔽 Aplicar heapify al nuevo root...")
            
            self.heapify(arr, i, 0, verbose)
            
            if verbose:
                self.visualizar_array_como_arbol(arr, i)
        
        if verbose:
            print("\n" + "="*70)
            print("✅ ARRAY ORDENADO COMPLETAMENTE")
            print("="*70)
            print(f"Resultado: {arr}")
            print(f"Total de operaciones: {self.pasos}")
        
        return arr


# ==================== DEMOSTRACIÓN PRÁCTICA ====================

def demo_basica():
    """
    Demo simple para entender el concepto.
    """
    print("\n" + "🎓 DEMO BÁSICA - Heap Sort Paso a Paso")
    print("="*70)
    
    arr = [4, 10, 3, 5, 1]
    print(f"\n📝 Vamos a ordenar: {arr}")
    
    hs = HeapSort()
    resultado = hs.heap_sort(arr.copy(), verbose=True)
    
    print(f"\n🎉 Resultado final: {resultado}")


def demo_comparacion():
    """
    Compara Heap Sort con otros algoritmos.
    """
    print("\n" + "⚔️  COMPARACIÓN DE ALGORITMOS")
    print("="*70)
    
    import time
    import random
    
    # Array grande para medir performance
    tamaños = [100, 1000, 5000]
    
    for n in tamaños:
        arr = [random.randint(1, 1000) for _ in range(n)]
        
        # Heap Sort
        arr_heap = arr.copy()
        inicio = time.time()
        hs = HeapSort()
        hs.heap_sort(arr_heap, verbose=False)
        tiempo_heap = time.time() - inicio
        
        # Python's sort (Timsort - O(n log n))
        arr_python = arr.copy()
        inicio = time.time()
        arr_python.sort()
        tiempo_python = time.time() - inicio
        
        print(f"\n📊 Array de {n} elementos:")
        print(f"   Heap Sort:   {tiempo_heap:.6f} segundos")
        print(f"   Python sort: {tiempo_python:.6f} segundos")
        print(f"   Operaciones Heap Sort: {hs.pasos}")


def demo_visualizacion_detallada():
    """
    Muestra cómo funciona heapify visualmente.
    """
    print("\n" + "🔬 DEMO DETALLADA - Entendiendo Heapify")
    print("="*70)
    
    arr = [3, 9, 2, 1, 4, 5]
    print(f"\nArray desordenado: {arr}")
    print("\nVamos a construir un Max Heap paso a paso...")
    
    hs = HeapSort()
    hs.build_max_heap(arr, verbose=True)
    
    print("\n💡 CONCEPTO CLAVE:")
    print("   - Max Heap: cada padre es MAYOR o IGUAL que sus hijos")
    print("   - Heapify: 'hunde' un nodo comparándolo con sus hijos")
    print("   - Si un hijo es mayor, hacemos swap y repetimos")


def demo_casos_especiales():
    """
    Casos edge: array ordenado, reverso, duplicados.
    """
    print("\n" + "🧪 CASOS ESPECIALES")
    print("="*70)
    
    hs = HeapSort()
    
    casos = {
        "Ya ordenado": [1, 2, 3, 4, 5],
        "Orden reverso": [5, 4, 3, 2, 1],
        "Duplicados": [3, 1, 3, 1, 3],
        "Un elemento": [42],
        "Array vacío": []
    }
    
    for nombre, arr in casos.items():
        print(f"\n📋 {nombre}: {arr}")
        arr_copia = arr.copy()
        hs.heap_sort(arr_copia, verbose=False)
        print(f"   Resultado: {arr_copia}")
        print(f"   ✅ Correcto: {arr_copia == sorted(arr)}")


# ==================== EXPLICACIÓN INTERACTIVA ====================

def explicacion_indices():
    """
    Explica cómo funcionan los índices en un heap.
    """
    print("\n" + "📚 ENTENDIENDO LOS ÍNDICES DEL HEAP")
    print("="*70)
    
    print("""
Un heap se representa como array pero se visualiza como árbol:

Array: [10, 5, 3, 4, 1]
Índices: 0   1  2  3  4

Como árbol:
        10 (índice 0)
       /  \\
      5    3  (índices 1, 2)
     / \\
    4   1     (índices 3, 4)

FÓRMULAS CLAVE:
- Padre de i:        (i - 1) // 2
- Hijo izquierdo:    2 * i + 1
- Hijo derecho:      2 * i + 2

EJEMPLOS:
- Nodo en índice 1 (valor 5):
  - Padre: (1-1)//2 = 0 → valor 10 ✅
  - Hijo izq: 2*1+1 = 3 → valor 4 ✅
  - Hijo der: 2*1+2 = 4 → valor 1 ✅

- Nodo en índice 3 (valor 4):
  - Padre: (3-1)//2 = 1 → valor 5 ✅
  - Hijo izq: 2*3+1 = 7 → no existe ✅
    """)


# ==================== EJECUTAR DEMOS ====================

if __name__ == "__main__":
    print("\n" + "🚀 HEAP SORT - TUTORIAL COMPLETO")
    print("="*70)
    
    # 1. Explicación de índices
    explicacion_indices()
    
    input("\n⏸️  Presiona ENTER para continuar con la demo básica...")
    
    # 2. Demo básica
    demo_basica()
    
    input("\n⏸️  Presiona ENTER para ver casos especiales...")
    
    # 3. Casos especiales
    demo_casos_especiales()
    
    input("\n⏸️  Presiona ENTER para comparación de performance...")
    
    # 4. Comparación
    demo_comparacion()
    
    input("\n⏸️  Presiona ENTER para demo detallada de heapify...")
    
    # 5. Heapify detallado
    demo_visualizacion_detallada()
    
    print("\n" + "="*70)
    print("🎉 TUTORIAL COMPLETADO")
    print("="*70)
    print("\n💡 PUNTOS CLAVE:")
    print("   ✅ Heap Sort usa un Max Heap (árbol donde padre >= hijos)")
    print("   ✅ Complejidad: O(n log n) en TODOS los casos")
    print("   ✅ Ordena in-place (no usa memoria extra)")
    print("   ✅ Heapify 'hunde' nodos para mantener propiedad heap")
    print("   ✅ Swap del root con el último, luego heapify")
    print("\n🚀 ¡Ahora intenta implementarlo en Go!")