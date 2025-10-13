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