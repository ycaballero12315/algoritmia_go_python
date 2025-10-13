package algoritmia


func Potencia(a int, b int) int {
	if (a==1 || b == 0) {
		return 1
	}
	return a*Potencia(a, b-1)
}

func Factorial(n int) int {
	if n<=0{
		return 0
	}
	if n==1 || n==0{
		return 1
	}
	return  n*Factorial(n-1)
}
