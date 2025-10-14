package algoritmia

func Potencia(a int, b int) int {
	if a == 1 || b == 0 {
		return 1
	}
	return a * Potencia(a, b-1)
}

func Factorial(n int) int {
	if n <= 0 {
		return 0
	}
	if n == 1 || n == 0 {
		return 1
	}
	return n * Factorial(n-1)
}

func DivVenceras(numbers []int, init int, end int) int {
	if init == end{
		return numbers[init]
	}
	medio := (init+end)/2
	left_numbers := DivVenceras(numbers, init, medio)
	rigth_number := DivVenceras(numbers, medio+1, end)
	return left_numbers + rigth_number
}

func Ackermann(m int, n int) int {
	temp:=0
	if (m==0){
		temp = n+1 
	}else{
		if (n==0){
			temp = Ackermann(m-1, 1)
		}else{
			temp = Ackermann(m-1, Ackermann(m, n-1))
		}
	}
	return temp
}

func Selection_sort(numeros []int, inicio int)  int{
	pos:= inicio
	for i := inicio+1; i < len(numeros); i++ {
		if numeros[i]<numeros[pos]{
			pos = i
		}
	}
	return  pos
}
