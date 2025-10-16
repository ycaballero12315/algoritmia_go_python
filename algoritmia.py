import random

def potencia(a:int, b:int)->int:
    if a==1 or b ==0:
        return 1
    return a* potencia(a, b-1)

print(potencia(2,5))

#factorial

def factorial(n:int)->int:
    if n <= -1:
        return 0
    if n==0 or n == 1:
        return 1
    return n*factorial(n-1)

print(factorial(-5))

def method(elems: list[int], init:int, end:int)->int:
    if init == end:
        return elems[init]
    medio = (init + end) // 2
    elemen_left = method(elems, init, medio)
    elemen_rigth = method(elems, medio+1, end)
    return elemen_left + elemen_rigth

print(method([4,5,6,7,3], 0, 4))

class Stack:
    def __init__(self) -> None:
        self.__data: list[int] = []

    def __push(self,elem:int)->None:
        self.__data.append(elem)
    
    def __pop(self)->int:
        if len(self.__data) == 0:
            return 0
        value = self.__data[len(self.__data) -1]
        self.__data = self.__data[:(len(self.data) - 1)]
        return value
    
    def __isEmty(self)->bool:
        return len(self.__data) == 0
    
    def __lenght(self)->int:
        return len(self.__data)
    
    # Getters and Setters
    @property
    def data(self)->list[int]:
        return self.__data.copy()
    
    def push(self, elem:int)->None:
        self.__push(elem)
    
    def peek(self)->int: #devuelve el untimo elemento sin modificar la pila
        if self.__isEmty():
            return 0
        return self.__data[-1]
    
    def pop(self)->int:
        return self.__pop()
    
    def isEmty(self)->bool:
        return self.__isEmty()
    
    def length(self)->int:
        return self.__lenght()
    
    @data.setter
    def data(self, new_data: list[int]) -> None:
        if not isinstance(new_data, list):
            raise TypeError("data debe ser una lista")
        if not all(isinstance(x, int) for x in new_data):
            raise TypeError("Todos los elementos deben ser enteros")
        self.__data = new_data.copy()

    def add(self, other_stack: 'Stack') -> 'Stack':
        
        if self.length() != other_stack.length():
            raise ValueError("Las pilas deben tener la misma longitud")
        
        result_stack = Stack()
        
        for i in range(self.length()):
            sum_value = self.data[i] + other_stack.data[i]
            result_stack.push(sum_value)
        
        return result_stack
    
    def __str__(self)->str:
        return f"Stack: {self.__data}"
    
if __name__ == "__main__":
    stack = Stack()
    stack2 = Stack()
    
    num_elements = random.randint(2, 10)
    print(f"Generando {num_elements} elementos aleatorios...\n")
    
    for _ in range(num_elements):
        value = random.randint(1, 100)
        stack.push(value)
        stack2.push(value)
    
    print(f"Stack 1: {stack}")
    print(f"Stack 2: {stack2}")
    print(f"Longitud: {stack.length()}\n")
    
    try:
        result_stack = stack.add(stack2)
        print(f"Resultado de la suma: {result_stack}")
        print(f"Stack 1 (sin modificar): {stack}")
        print(f"Stack 2 (sin modificar): {stack2}")
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\n" + "="*50 + "\n")