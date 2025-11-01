# ============================================
# GRAFOS - IMPLEMENTACIÓN COMPLETA
# Por: Dalto Style 😎
# ============================================

from collections import deque, defaultdict
import heapq

# ============================================
# 1. GRAFO CON LISTA DE ADYACENCIA
# La forma más eficiente en la mayoría de casos
# ============================================

class Grafo:
    def __init__(self, dirigido=False):
        """
        dirigido: True si el grafo es dirigido, False si no
        """
        self.grafo = defaultdict(list)  # Diccionario que contiene listas
        self.dirigido = dirigido
        
    def agregar_arista(self, origen, destino, peso=1):
        """
        Agrega una arista (conexión) entre dos nodos
        """
        self.grafo[origen].append((destino, peso))
        
        # Si no es dirigido, agregamos la conexión inversa
        if not self.dirigido:
            self.grafo[destino].append((origen, peso))
    
    def mostrar_grafo(self):
        """
        Muestra la estructura del grafo
        """
        for nodo in self.grafo:
            conexiones = [f"{dest}(peso:{peso})" for dest, peso in self.grafo[nodo]]
            print(f"{nodo} -> {', '.join(conexiones)}")
    
    # ============================================
    # BFS - BÚSQUEDA EN AMPLITUD (Breadth-First Search)
    # Explora nivel por nivel, como ondas en el agua
    # ============================================
    
    def bfs(self, inicio):
        """
        Recorre el grafo nivel por nivel
        Usa una COLA (Queue) - FIFO
        """
        visitados = set()
        cola = deque([inicio])
        visitados.add(inicio)
        recorrido = []
        
        while cola:
            nodo = cola.popleft()  # Sacamos el primero (FIFO)
            recorrido.append(nodo)
            
            # Exploramos los vecinos
            for vecino, _ in self.grafo[nodo]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        
        return recorrido
    
    # ============================================
    # DFS - BÚSQUEDA EN PROFUNDIDAD (Depth-First Search)
    # Va lo más profundo posible antes de retroceder
    # ============================================
    
    def dfs(self, inicio):
        """
        Recorre el grafo explorando en profundidad
        Usa una PILA (Stack) - LIFO
        """
        visitados = set()
        pila = [inicio]
        recorrido = []
        
        while pila:
            nodo = pila.pop()  # Sacamos el último (LIFO)
            
            if nodo not in visitados:
                visitados.add(nodo)
                recorrido.append(nodo)
                
                # Agregamos vecinos a la pila
                for vecino, _ in self.grafo[nodo]:
                    if vecino not in visitados:
                        pila.append(vecino)
        
        return recorrido
    
    def dfs_recursivo(self, inicio, visitados=None):
        """
        DFS de forma recursiva (más elegante)
        """
        if visitados is None:
            visitados = set()
        
        visitados.add(inicio)
        recorrido = [inicio]
        
        for vecino, _ in self.grafo[inicio]:
            if vecino not in visitados:
                recorrido.extend(self.dfs_recursivo(vecino, visitados))
        
        return recorrido
    
    # ============================================
    # DIJKSTRA - CAMINO MÁS CORTO
    # Encuentra el camino más corto desde un nodo a todos los demás
    # ============================================
    
    def dijkstra(self, inicio):
        """
        Algoritmo de Dijkstra para encontrar el camino más corto
        """
        distancias = {nodo: float('inf') for nodo in self.grafo}
        distancias[inicio] = 0
        
        # Cola de prioridad: (distancia, nodo)
        cola_prioridad = [(0, inicio)]
        visitados = set()
        
        while cola_prioridad:
            dist_actual, nodo_actual = heapq.heappop(cola_prioridad)
            
            if nodo_actual in visitados:
                continue
                
            visitados.add(nodo_actual)
            
            # Exploramos vecinos
            for vecino, peso in self.grafo[nodo_actual]:
                distancia = dist_actual + peso
                
                # Si encontramos un camino más corto, lo actualizamos
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    heapq.heappush(cola_prioridad, (distancia, vecino))
        
        return distancias
    
    # ============================================
    # DETECCIÓN DE CICLOS
    # Detecta si hay ciclos en el grafo
    # ============================================
    
    def tiene_ciclo(self):
        """
        Detecta si el grafo tiene ciclos (para grafos dirigidos)
        """
        visitados = set()
        rec_stack = set()
        
        def dfs_ciclo(nodo):
            visitados.add(nodo)
            rec_stack.add(nodo)
            
            for vecino, _ in self.grafo[nodo]:
                if vecino not in visitados:
                    if dfs_ciclo(vecino):
                        return True
                elif vecino in rec_stack:
                    return True
            
            rec_stack.remove(nodo)
            return False
        
        for nodo in self.grafo:
            if nodo not in visitados:
                if dfs_ciclo(nodo):
                    return True
        
        return False


# ============================================
# EJEMPLOS PRÁCTICOS - APRENDÉ VIENDO
# ============================================

def ejemplo_red_social():
    """
    Ejemplo: Red social (grafo no dirigido)
    """
    print("\n" + "="*50)
    print("EJEMPLO 1: RED SOCIAL")
    print("="*50)
    
    red = Grafo(dirigido=False)
    
    # Agregamos amistades
    red.agregar_arista("Dalto", "Juan")
    red.agregar_arista("Dalto", "Maria")
    red.agregar_arista("Juan", "Pedro")
    red.agregar_arista("Maria", "Pedro")
    red.agregar_arista("Pedro", "Lucas")
    
    print("\nEstructura de la red:")
    red.mostrar_grafo()
    
    print("\nAmigos de Dalto (BFS):", red.bfs("Dalto"))
    print("Amigos de Dalto (DFS):", red.dfs("Dalto"))


def ejemplo_mapa_ciudades():
    """
    Ejemplo: Mapa de ciudades con distancias (grafo ponderado)
    """
    print("\n" + "="*50)
    print("EJEMPLO 2: MAPA DE CIUDADES")
    print("="*50)
    
    mapa = Grafo(dirigido=False)
    
    # Agregamos rutas con distancias en km
    mapa.agregar_arista("Buenos Aires", "Rosario", 300)
    mapa.agregar_arista("Buenos Aires", "Montevideo", 200)
    mapa.agregar_arista("Rosario", "Córdoba", 400)
    mapa.agregar_arista("Córdoba", "Mendoza", 600)
    mapa.agregar_arista("Montevideo", "Rosario", 450)
    
    print("\nRutas disponibles:")
    mapa.mostrar_grafo()
    
    print("\nDistancias más cortas desde Buenos Aires:")
    distancias = mapa.dijkstra("Buenos Aires")
    for ciudad, dist in distancias.items():
        print(f"  {ciudad}: {dist} km")


def ejemplo_dependencias():
    """
    Ejemplo: Dependencias de tareas (grafo dirigido)
    """
    print("\n" + "="*50)
    print("EJEMPLO 3: DEPENDENCIAS DE TAREAS")
    print("="*50)
    
    tareas = Grafo(dirigido=True)
    
    # Una tarea puede depender de otra
    tareas.agregar_arista("Diseño", "Desarrollo")
    tareas.agregar_arista("Desarrollo", "Testing")
    tareas.agregar_arista("Testing", "Deploy")
    tareas.agregar_arista("Diseño", "Documentación")
    
    print("\nDependencias:")
    tareas.mostrar_grafo()
    
    print("\nOrden de ejecución (DFS desde Diseño):", tareas.dfs("Diseño"))
    
    print("\n¿Tiene ciclos?", tareas.tiene_ciclo())


# ============================================
# EJECUTAR EJEMPLOS
# ============================================

if __name__ == "__main__":
    print("🎯 GRAFOS - LA GUÍA DEFINITIVA 🎯")
    
    ejemplo_red_social()
    ejemplo_mapa_ciudades()
    ejemplo_dependencias()
    
    print("\n" + "="*50)
    print("✅ ¡Terminamos! Ahora sabés grafos como un crack")
    print("="*50)