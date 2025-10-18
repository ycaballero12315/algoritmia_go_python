def analizar_texto(texto:str):

    frecuencias = {}  # HashMap vacío

    palabras = texto.lower().split()
    for palabra in palabras:
        # Patrón común: get con valor default
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    return frecuencias
texto = "Hola a todos mundo soft hola"
print(texto.lower().split())
print(analizar_texto(texto))

from collections import defaultdict


text = "Python es fenomenal, su sintaxis sencilla y su amplio uso lo convierte en unos de los mejores lenguajes"
frecuencia = defaultdict(int)
for palabra in text.lower().split():
    frecuencia[palabra] += 1

print(frecuencia)

# fibonnasi con cache
def fibonassi_with_cache(n: int, cache=None)->int:
    if cache is None:
        cache = {}

    if n in cache:
        return cache[n]

    if n <= 1:
        return n

    cache[n] = fibonassi_with_cache(n - 1, cache) + fibonassi_with_cache(n - 2, cache)
    return cache[n]


print(f"Fibonacci de 100: {fibonassi_with_cache(100)}")

def crear_indice_invertido(documentos):
    """
    Crea un índice invertido como los motores de búsqueda.
    
    Índice invertido: palabra → lista de documentos que la contienen
    """
    indice = defaultdict(list)
    
    for doc_id, contenido in documentos.items():
        palabras = contenido.lower().split()
        for palabra in palabras:
            if doc_id not in indice[palabra]:
                indice[palabra].append(doc_id)
    
    return indice

documentos = {
    1: "La casa azul",
    2: "La casa verde",
    3: "El perro azul",
}

indice = crear_indice_invertido(documentos)

for palabra, docs in indice.items():
    print(f"{palabra}: {docs}")

def buscar(indice, termino):
    """
    Busca documentos que contienen un término.
    Complejidad: O(1) - ¡Búsqueda instantánea!
    """
    return indice.get(termino.lower(), [])

# Documentos de ejemplo
docs = {
    "doc1": "Python es un lenguaje de programación",
    "doc2": "Go es un lenguaje compilado",
    "doc3": "Python y Go son lenguajes modernos"
}
# print(docs.__sizeof__())
indice = crear_indice_invertido(docs)
print(indice)
print(f"\n🔍 Documentos con 'python': {buscar(indice, 'python')}")
print(f"🔍 Documentos con 'lenguaje': {buscar(indice, 'lenguaje')}")

documentos = {
    1: 'Ossany es mi amigo',
    2: 'Ossany es una muy buena persona',
    3: 'Ossany e Irene son las mejores personas que he conocido',
    4: 'Ossany e irene tienen a su ninno esteban'
}

def hashmap_invertido(documentos:dict[int, str]):
    indices = defaultdict()

    for d_id, palabras in documentos:
        palabra = palabras.lower().split()
        if palabra not in indices[palabra]:
            indices[palabra].append(d_id)
    
    return indices

productos = [
    {'nombre': 'Laptop', 'tipo': 'electrónica', 'precio': 1000},
    {'nombre': 'Mouse', 'tipo': 'electrónica', 'precio': 25},
    {'nombre': 'Silla', 'tipo': 'mueble', 'precio': 150},
    {'nombre': 'Escritorio', 'tipo': 'mueble', 'precio': 300},
]

def agrupar_categoria(productos):
    grupos = defaultdict(list)
    for p in productos:
        categoria = p['tipo']
        grupos[categoria].append(p)
    
    return dict(grupos)

grupos = agrupar_categoria(productos)
print(type(grupos))

for cat, prod in grupos.items():
    print(f"los elementos de esta categiria: {cat}:")
    for item in prod:
        print(f"  - {item['nombre']} (${item['precio']})")

def delete_duplicates(lista):
    result = []
    unicos = {}

    for item in lista:
        if item not in unicos:
            unicos[item] = True
            result.append(item)

    return result

list_elem_rep = [3,4,6,4,3,8,3]
print(f'Elementos unicos: {delete_duplicates(list_elem_rep)}')