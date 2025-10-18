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
	fmt.Printf("El fibonassi es: %d\n", algoritmia.Fibonnacci(5))
	fmt.Printf("Elemento insertado en la lista %d\n", algoritmia.AddElms(40))
	fmt.Printf("Elemento eliminado: %d\n", algoritmia.PopElm())
	fmt.Printf("Existe el numero 20?: %v\n", algoritmia.IsNumExist(20))
	fmt.Printf("Tamanno de la lista: %d\n", algoritmia.Length())
	algoritmia.AddElms(40)
	fmt.Printf("El ultimo elemento es: %d\n", algoritmia.PopElm())

    lkl := &algoritmia.LinkedList{}
	lkl.AddNodeInEndList("A")
	lkl.AddNodeInEndList("B")
	lkl.AddNodeInEndList("C")

	for value := range lkl.Values() {
		fmt.Println(value)
	}
	fmt.Printf("Haciendo pruebas con hashmap: %d\n", algoritmia.HashMap("yoe"))
}
