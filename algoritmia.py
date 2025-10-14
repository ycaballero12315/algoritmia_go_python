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