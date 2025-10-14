package main

import (
	"algoritmia/algoritmia"
	"fmt"
)

func main() {
	fmt.Printf("La potencia es: %d\n", algoritmia.Potencia(2, 5))
	fmt.Printf("El factorial se %d\n", algoritmia.Factorial(5))
	fmt.Printf("Algoritmo divide y venceras: %d\n", algoritmia.DivVenceras([]int{2, 5, 6, 7, 23}, 0, 4))
	fmt.Printf("El metodo extranno Ackerman: %d\n", algoritmia.Ackermann(1, 2))
	fmt.Printf("El menor numero esta en posicion: %d\n", algoritmia.Selection_sort([]int{2, 5, 6, 7, 23}, 0))
}
