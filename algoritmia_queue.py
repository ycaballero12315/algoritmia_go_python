from collections import deque

class QueveOtimized:
    def __init__(self):
        self.elements = deque()
    
    def enqueve(self, elem: int)->None:
        self.elements.append(elem)
    
    def isEmty(self)->bool:
        return len(self.elements) == 0
    
    def dequeve(self)->int:
        if self.isEmty():
            raise ValueError('list Empty, not exist element')
        return self.elements.popleft()
    
    def peek(self)->int:
        if self.isEmty():
            raise ValueError('list Empty, not exist element')
        return self.elements[0]
    
    def __str__(self)->str:
        return f"Queve: {list(self.elements)}"
    
    def __len__(self)->int:
        return len(self.elements)
    
    def clear(self):
        self.elements.clear()
    