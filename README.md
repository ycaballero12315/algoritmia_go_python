# Linked Lists: Implementación Comparativa Go vs Python

> Mismo concepto, dos lenguajes, diferentes filosofías de diseño

---

## 📋 Tabla de Contenidos

1. [Introducción](#introducción)
2. [Implementación en Go](#implementación-en-go)
3. [Implementación en Python](#implementación-en-python)
4. [Análisis Comparativo](#análisis-comparativo)
5. [Complejidad Algorítmica](#complejidad-algorítmica)
6. [Ejemplos de Uso](#ejemplos-de-uso)

---

## 🎯 Introducción

Una **Lista Enlazada Simple** (Singly Linked List) es una estructura de datos lineal donde cada elemento (nodo) contiene:
- Un valor (data)
- Una referencia al siguiente nodo (next)

```
head -> [A] -> [B] -> [C] -> [D] -> nil/None
```

### Ventajas
- ✅ Inserción/eliminación O(1) al inicio
- ✅ Tamaño dinámico
- ✅ No requiere memoria contigua

### Desventajas
- ❌ Acceso O(n) por índice
- ❌ Mayor uso de memoria (punteros/referencias)
- ❌ No hay acceso aleatorio eficiente

---

## 🔷 Implementación en Go

### Estructura de Datos

```go
package main

import "fmt"

// Node representa un nodo individual de la lista
type Node struct {
    value string
    next  *Node
}

// LinkedList representa la lista enlazada
type LinkedList struct {
    head *Node
}
```

### Constructor

```go
// NewLinkedList crea una nueva lista enlazada vacía
func NewLinkedList() *LinkedList {
    return &LinkedList{head: nil}
}
```

### Método: Agregar Nodo al Final

```go
// AddNodeInEndList agrega un nodo al final de la lista
// Complejidad: O(n)
func (l *LinkedList) AddNodeInEndList(value string) {
    newNode := &Node{value: value, next: nil}
    
    // Caso 1: Lista vacía
    if l.head == nil {
        l.head = newNode
        return
    }
    
    // Caso 2: Recorrer hasta el final
    current := l.head
    for current.next != nil {
        current = current.next
    }
    
    current.next = newNode
}
```

### Método: Agregar al Inicio

```go
// AddNodeAtBeginning agrega un nodo al inicio
// Complejidad: O(1)
func (l *LinkedList) AddNodeAtBeginning(value string) {
    newNode := &Node{value: value, next: l.head}
    l.head = newNode
}
```

### Método: Eliminar Nodo por Valor

```go
// DeleteNode elimina la primera ocurrencia de un nodo con el valor dado
// Complejidad: O(n)
func (l *LinkedList) DeleteNode(value string) bool {
    // Caso 1: Lista vacía
    if l.head == nil {
        return false
    }
    
    // Caso 2: Eliminar el head
    if l.head.value == value {
        l.head = l.head.next
        return true
    }
    
    // Caso 3: Buscar en el resto de la lista
    current := l.head
    for current.next != nil {
        if current.next.value == value {
            current.next = current.next.next
            return true
        }
        current = current.next
    }
    
    return false
}
```

### Método: Buscar Valor

```go
// Search verifica si un valor existe en la lista
// Complejidad: O(n)
func (l *LinkedList) Search(value string) bool {
    current := l.head
    for current != nil {
        if current.value == value {
            return true
        }
        current = current.next
    }
    return false
}
```

### Método: Insertar Después de un Valor

```go
// InsertAfter inserta un nuevo nodo después del primer nodo con el valor dado
// Complejidad: O(n)
func (l *LinkedList) InsertAfter(target string, value string) bool {
    current := l.head
    for current != nil {
        if current.value == target {
            newNode := &Node{value: value, next: current.next}
            current.next = newNode
            return true
        }
        current = current.next
    }
    return false
}
```

### Método: Obtener Longitud

```go
// Length retorna la cantidad de nodos en la lista
// Complejidad: O(n)
func (l *LinkedList) Length() int {
    count := 0
    current := l.head
    for current != nil {
        count++
        current = current.next
    }
    return count
}
```

### Método: Verificar si está Vacía

```go
// IsEmpty verifica si la lista está vacía
// Complejidad: O(1)
func (l *LinkedList) IsEmpty() bool {
    return l.head == nil
}
```

### Método: Iteración con Channels (Go idiomático)

```go
// Values retorna un channel para iterar sobre los valores
// Patrón concurrente con goroutines
func (l *LinkedList) Values() <-chan string {
    ch := make(chan string)
    
    go func() {
        current := l.head
        for current != nil {
            ch <- current.value
            current = current.next
        }
        close(ch)
    }()
    
    return ch
}
```

### Método: Convertir a Slice

```go
// ToSlice convierte la lista enlazada a un slice de Go
// Complejidad: O(n)
func (l *LinkedList) ToSlice() []string {
    var result []string
    current := l.head
    for current != nil {
        result = append(result, current.value)
        current = current.next
    }
    return result
}
```

### Método: Imprimir Lista

```go
// String implementa la interfaz Stringer
func (l *LinkedList) String() string {
    if l.head == nil {
        return "[]"
    }
    
    values := l.ToSlice()
    return fmt.Sprintf("%v", values)
}
```

### Método: Limpiar Lista

```go
// Clear vacía completamente la lista
// Complejidad: O(1) gracias al GC
func (l *LinkedList) Clear() {
    l.head = nil
}
```

### Ejemplo de Uso - Go

```go
func main() {
    // Crear lista
    list := NewLinkedList()
    
    // Agregar elementos
    list.AddNodeInEndList("A")
    list.AddNodeInEndList("B")
    list.AddNodeInEndList("C")
    list.AddNodeAtBeginning("START")
    
    fmt.Println("Lista:", list)
    fmt.Println("Longitud:", list.Length())
    
    // Insertar después de un valor
    list.InsertAfter("A", "X")
    fmt.Println("Después de insertar X:", list)
    
    // Buscar
    fmt.Println("¿Contiene 'B'?", list.Search("B"))
    
    // Eliminar
    list.DeleteNode("B")
    fmt.Println("Después de eliminar B:", list)
    
    // Iterar con channels
    fmt.Println("\nIterando con channels:")
    for value := range list.Values() {
        fmt.Printf("  -> %s\n", value)
    }
}
```

---

## 🐍 Implementación en Python

### Estructura de Datos

```python
class Node:
    """
    Nodo individual de la lista enlazada.
    
    Attributes:
        value: Valor almacenado en el nodo
        next: Referencia al siguiente nodo
    """
    def __init__(self, value: int):
        self.value = value
        self.next = None
    
    def __repr__(self) -> str:
        return f"Node({self.value})"


class LinkedList:
    """
    Lista Enlazada Simple.
    
    Attributes:
        head: Primer nodo de la lista (None si está vacía)
    """
    def __init__(self):
        """Inicializa una lista vacía."""
        self.head = None
```

### Método: Agregar Nodo al Final

```python
def add_node_in_end_list(self, value: int) -> None:
    """
    Agrega un nodo al final de la lista.
    
    Complejidad: O(n)
    
    Args:
        value: Valor del nuevo nodo
    """
    new_node = Node(value)
    
    # Caso 1: Lista vacía
    if self.head is None:
        self.head = new_node
        return
    
    # Caso 2: Recorrer hasta el final
    current = self.head
    while current.next is not None:
        current = current.next
    
    current.next = new_node
```

### Método: Agregar al Inicio

```python
def add_node_at_beginning(self, value: int) -> None:
    """
    Agrega un nodo al inicio de la lista.
    
    Complejidad: O(1)
    """
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node
```

### Método: Eliminar Nodo por Valor

```python
def delete_node_match_value(self, value: int) -> bool:
    """
    Elimina la primera ocurrencia de un nodo con el valor dado.
    
    Complejidad: O(n)
    
    Args:
        value: Valor del nodo a eliminar
    
    Returns:
        True si se eliminó, False si no se encontró
    """
    # Caso 1: Lista vacía
    if self.head is None:
        return False
    
    # Caso 2: Eliminar el head
    if self.head.value == value:
        self.head = self.head.next
        return True
    
    # Caso 3: Buscar en el resto
    current = self.head
    while current.next is not None:
        if current.next.value == value:
            current.next = current.next.next
            return True
        current = current.next
    
    return False
```

### Método: Buscar Valor

```python
def search(self, value: int) -> bool:
    """
    Busca si un valor existe en la lista.
    
    Complejidad: O(n)
    """
    current = self.head
    while current is not None:
        if current.value == value:
            return True
        current = current.next
    return False
```

### Método: Insertar en Posición Específica

```python
def insert_in_the_wherever_in_position(self, target_value: int, value: int) -> bool:
    """
    Inserta un nuevo nodo después del primer nodo con target_value.
    
    Complejidad: O(n)
    
    Args:
        target_value: Valor después del cual insertar
        value: Valor del nuevo nodo
    
    Returns:
        True si se insertó, False si no se encontró target_value
    """
    current = self.head
    while current is not None:
        if current.value == target_value:
            new_node = Node(value)
            new_node.next = current.next
            current.next = new_node
            return True
        current = current.next
    return False
```

### Método: Obtener Longitud

```python
def length(self) -> int:
    """
    Retorna la cantidad de nodos en la lista.
    
    Complejidad: O(n)
    """
    count = 0
    current = self.head
    while current is not None:
        count += 1
        current = current.next
    return count
```

### Método: Verificar si está Vacía

```python
def is_empty(self) -> bool:
    """
    Verifica si la lista está vacía.
    
    Complejidad: O(1)
    """
    return self.head is None
```

### Método: Iteración con Generator (Python idiomático)

```python
def print_values(self):
    """
    Generator que produce los valores de la lista uno por uno.
    
    Yields:
        Valor de cada nodo
    
    Example:
        >>> for value in lista.print_values():
        ...     print(value)
    """
    current = self.head
    while current:
        yield current.value
        current = current.next
```

### Método: Convertir a Lista

```python
def to_list(self) -> list[int]:
    """
    Convierte la lista enlazada a una lista de Python.
    
    Complejidad: O(n)
    """
    return list(self.print_values())
```

### Método: Representación en String

```python
def __str__(self) -> str:
    """Representación en string de la lista."""
    if self.head is None:
        return "[]"
    
    values = []
    current = self.head
    while current is not None:
        values.append(str(current.value))
        current = current.next
    
    return " -> ".join(values)

def __repr__(self) -> str:
    """Representación oficial para debugging."""
    return f"LinkedList({self.to_list()})"
```

### Método: Limpiar Lista

```python
def clear(self) -> None:
    """
    Vacía completamente la lista.
    
    Complejidad: O(1)
    """
    self.head = None
```

### Ejemplo de Uso - Python

```python
if __name__ == "__main__":
    # Crear lista
    lkl = LinkedList()
    
    # Agregar elementos
    lkl.add_node_in_end_list("A")
    lkl.add_node_in_end_list("B")
    lkl.add_node_in_end_list("C")
    lkl.add_node_at_beginning("START")
    
    print(f"Lista: {lkl}")
    print(f"Longitud: {lkl.length()}")
    
    # Insertar después de un valor
    lkl.insert_in_the_wherever_in_position("A", "X")
    print(f"Después de insertar X: {list(lkl.print_values())}")
    
    # Buscar
    print(f"¿Contiene 'B'? {lkl.search('B')}")
    
    # Eliminar
    lkl.delete_node_match_value("B")
    print(f"Después de eliminar B: {list(lkl.print_values())}")
    
    # Iterar con generator
    print("\nIterando con generator:")
    for value in lkl.print_values():
        print(f"  -> {value}")
```

---

## ⚖️ Análisis Comparativo

### Sintaxis y Paradigmas

| Aspecto | Go | Python |
|---------|----|----|
| **Tipos** | Estáticos, explícitos | Dinámicos, implícitos |
| **Punteros** | Explícitos (`*Node`) | Implícitos (referencias) |
| **Memory Management** | GC + control manual | GC automático |
| **Iteración** | Channels + goroutines | Generators + yield |
| **Error Handling** | Retorno múltiple | Excepciones |
| **Nil/None** | `nil` | `None` |

### Características Idiomáticas

#### Go
```go
// Pattern: Channel-based iteration
func (l *LinkedList) Values() <-chan string {
    ch := make(chan string)
    go func() {
        // Goroutine maneja la iteración
        for current := l.head; current != nil; current = current.next {
            ch <- current.value
        }
        close(ch)
    }()
    return ch
}
```

**Ventajas:**
- ✅ Non-blocking iteration
- ✅ Concurrent consumption
- ✅ Backpressure natural

#### Python
```python
# Pattern: Generator-based iteration
def print_values(self):
    current = self.head
    while current:
        yield current.value
        current = current.next
```

**Ventajas:**
- ✅ Lazy evaluation
- ✅ Memory efficient
- ✅ Sintaxis simple

### Performance

| Operación | Go | Python |
|-----------|----|----|
| **Inserción** | ~20-50 ns | ~100-200 ns |
| **Búsqueda** | ~30-70 ns | ~150-300 ns |
| **Iteración** | ~40-80 ns/elem | ~200-400 ns/elem |
| **Memory overhead** | ~24 bytes/node | ~56 bytes/node |

*Benchmarks aproximados en hardware moderno*

### Lines of Code (LOC)

```
Go:     ~150 líneas (con comentarios)
Python: ~120 líneas (con comentarios)

Ratio: Python ~20% más conciso
```

---

## 📊 Complejidad Algorítmica

### Temporal

| Operación | Complejidad | Descripción |
|-----------|-------------|-------------|
| `AddNodeInEndList` | **O(n)** | Debe recorrer hasta el final |
| `AddNodeAtBeginning` | **O(1)** | Acceso directo al head |
| `DeleteNode` | **O(n)** | Worst case: elemento al final |
| `Search` | **O(n)** | Debe revisar todos los nodos |
| `InsertAfter` | **O(n)** | Buscar + inserción |
| `Length` | **O(n)** | Contar todos los nodos |
| `IsEmpty` | **O(1)** | Verificar si head es nil/None |
| `Values/Iteration` | **O(n)** | Recorrer todos |

### Espacial

| Operación | Go | Python |
|-----------|----|----|
| **Estructura base** | O(n) | O(n) |
| **Iteración (channel)** | O(k) buffer | - |
| **Iteración (generator)** | - | O(1) |
| **Total** | O(n) | O(n) |

donde:
- `n` = número de nodos
- `k` = tamaño del buffer del channel (si es buffered)

---

## 🚀 Ejemplos de Uso Avanzados

### Go: Uso con Concurrencia

```go
func main() {
    list := NewLinkedList()
    list.AddNodeInEndList("A")
    list.AddNodeInEndList("B")
    list.AddNodeInEndList("C")
    
    // Procesar valores concurrentemente
    done := make(chan bool)
    
    go func() {
        for value := range list.Values() {
            fmt.Printf("Procesando: %s\n", value)
            time.Sleep(100 * time.Millisecond)
        }
        done <- true
    }()
    
    <-done
    fmt.Println("Procesamiento completado")
}
```

### Python: Uso con Comprehensions

```python
# Crear lista
lkl = LinkedList()
for i in range(1, 6):
    lkl.add_node_in_end_list(i)

# List comprehension con generator
squares = [x**2 for x in lkl.print_values()]
print(f"Cuadrados: {squares}")

# Filter con generator
evens = [x for x in lkl.print_values() if x % 2 == 0]
print(f"Pares: {evens}")

# Sum con generator
total = sum(lkl.print_values())
print(f"Suma total: {total}")
```

### Go: Pipeline Pattern

```go
// Filtrar valores
func FilterValues(list *LinkedList, predicate func(string) bool) *LinkedList {
    filtered := NewLinkedList()
    for value := range list.Values() {
        if predicate(value) {
            filtered.AddNodeInEndList(value)
        }
    }
    return filtered
}

// Uso
list := NewLinkedList()
list.AddNodeInEndList("apple")
list.AddNodeInEndList("banana")
list.AddNodeInEndList("apricot")

startsWithA := FilterValues(list, func(s string) bool {
    return strings.HasPrefix(s, "a")
})
```

### Python: Functional Programming

```python
from functools import reduce

# Map
def map_values(lkl, func):
    result = LinkedList()
    for value in lkl.print_values():
        result.add_node_in_end_list(func(value))
    return result

# Filter
def filter_values(lkl, predicate):
    result = LinkedList()
    for value in lkl.print_values():
        if predicate(value):
            result.add_node_in_end_list(value)
    return result

# Reduce
def reduce_values(lkl, func, initial):
    return reduce(func, lkl.print_values(), initial)

# Uso
lkl = LinkedList()
for i in [1, 2, 3, 4, 5]:
    lkl.add_node_in_end_list(i)

doubled = map_values(lkl, lambda x: x * 2)
evens = filter_values(lkl, lambda x: x % 2 == 0)
sum_all = reduce_values(lkl, lambda a, b: a + b, 0)
```

---

## 🎓 Conclusiones

### Cuándo Usar Cada Lenguaje

**Elige Go si necesitas:**
- ✅ Performance crítico
- ✅ Concurrencia nativa
- ✅ Type safety en compile-time
- ✅ Binarios standalone
- ✅ Servicios de alta carga

**Elige Python si necesitas:**
- ✅ Desarrollo rápido
- ✅ Prototipado ágil
- ✅ Ecosistema rico (ML, data science)
- ✅ Código conciso y expresivo
- ✅ Scripts y automatización

### Lecciones Aprendidas

1. **Los conceptos son universales**: La lógica de la lista enlazada es idéntica
2. **La sintaxis es superficial**: Go usa `*` para punteros, Python no
3. **Los idioms importan**: Channels en Go, generators en Python
4. **Performance vs Productividad**: Trade-off eterno
5. **El mejor lenguaje**: Es el que tu equipo domina y el problema requiere

---

## 📝 Licencia

MIT License - Úsalo, modifícalo, aprende de él.

---

**Autor**: [Yoeny caballero Gonzalez]  
**Fecha**: 16-10-2025  
**Tags**: #DataStructures #Go #Python #LinkedList #Algorithms

---

*"El código es temporal, los conceptos son eternos"*