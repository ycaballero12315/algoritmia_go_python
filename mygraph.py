from collections import deque

class Vertex:
    def __init__(self):
        self.__name = None
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"Vertex: {self.name}"
    
    def __eq__(self, other):
        return isinstance(other, Vertex) and self.name == other.name
    
    def __hash__(self):
        return hash(self.name)

class Edge:
    def __init__(self):
        self.__start = None
        self.__end = None
    
    @property
    def start(self):
        return self.__start
    @property
    def end(self):
        return self.__end
    @start.setter
    def start(self, start):
        self.__start = start
    @end.setter
    def end(self, end):
        self.__end = end

class Graph:
    def __init__(self):
        self.graph_dict = {}
    
    def add_vertex(self, vertex:Vertex):
        if vertex in self.graph_dict:
            raise ValueError (f"Vertex is exist")
        self.graph_dict[vertex] = []
    
    def add_edge(self, edge:Edge):
        start = edge.start
        end = edge.end
        if start not in self.graph_dict or end not in self.graph_dict:
            raise ValueError('Ambos vertices deben existir en el grafo antes de crear la edge')
        if end not in self.graph_dict[start]:
            self.graph_dict[start].append(end)
    
    # --- DFS (Depth First Search) Busqueda en Profundidad ---
    def dfs(self, start, target=None, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)

        if target is not None and start == target:
            return True
        
        for neighbor in self.graph_dict[start]:
            if neighbor not in visited:
                found = self.dfs(neighbor, target, visited)
                if target is not None and found:
                    return True
        return visited if target is None else False
    
     # --- BFS (Breadth First Search) Busqueda en anchura---
    def bfs(self, start, target=None):
        visited = set()
        queue = deque([start])

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                if target is not None and vertex == target:
                    return True
                for neighbor in self.graph_dict[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return visited if target is None else False

#Creando los vertices
a = Vertex()
a.name = "A"
b = Vertex()
b.name = "B"
c = Vertex()
c.name = "C"
d = Vertex()
d.name = 'D'

g = Graph()
for v in (a, b, c, d):
    g.add_vertex(v)

# Creando los edge
e1 = Edge(); e1.start = a; e1.end = b
e2 = Edge(); e2.start = a; e2.end = c
e3 = Edge(); e3.start = b; e3.end = d
g.add_edge(e1)
g.add_edge(e2)
g.add_edge(e3)

print("DFS:", [v.name for v in g.dfs(a)])
print("BFS:", [v.name for v in g.bfs(a)])

# Búsqueda de destino
print("¿Hay camino de A a D?", g.dfs(a, d))

