package algoritmia

import (
	"slices"
	"fmt"
	// "golang.org/x/tools/go/analysis/passes/appends"
)

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
	if init == end {
		return numbers[init]
	}
	medio := (init + end) / 2
	left_numbers := DivVenceras(numbers, init, medio)
	rigth_number := DivVenceras(numbers, medio+1, end)
	return left_numbers + rigth_number
}

func Ackermann(m int, n int) int {
	temp := 0
	if m == 0 {
		temp = n + 1
	} else {
		if n == 0 {
			temp = Ackermann(m-1, 1)
		} else {
			temp = Ackermann(m-1, Ackermann(m, n-1))
		}
	}
	return temp
}

func Selection_sort(numeros []int, inicio int) int {
	pos := inicio
	for i := inicio + 1; i < len(numeros); i++ {
		if numeros[i] < numeros[pos] {
			pos = i
		}
	}
	return pos
}

func Fibonnacci(n int) int {
	if n == 0 {
		return 0
	}
	if n == 1 {
		return 1
	}
	return Fibonnacci(n-1) + Fibonnacci(n-2)
}

type StackInt struct{
	data []int
}

func (stack *StackInt) Push(value int)(){
	stack.data = append(stack.data, value)
}

func (stack *StackInt) Pop() (int, bool) {
	if len(stack.data) == 0{
		return 0, false
	}
	value := stack.data[len(stack.data)-1]
	stack.data = stack.data[:len(stack.data)-1]
	return value, true
}

func (stack *StackInt)  IsEmty() bool{
	return len(stack.data) == 0
}

func (stack *StackInt) Len() int{
	return len(stack.data)
}

func (stack *StackInt) Add(stack1 *StackInt) *StackInt{
	if len(stack.data) != len(stack1.data){
		fmt.Printf("Las pilas tienen que tener la misma longitud.")
		return nil
	}
	result := &StackInt{}
	for i := 0; i < len(stack.data); i++ {
		sum := stack.data[i] + stack1.data[i]
		result.Push(sum)
	}
	return  result
}

var numbers = []int{10,20,30}

func AddElms(value int) []int{
	numbers = append(numbers, value)
	return numbers
}

func PopElm() int{
	if len(numbers) == 0{
		return 0
	}
	value := numbers[len(numbers) -1]
	numbers = numbers[:len(numbers) -1]
	return value
}
func IsNumExist(value int) bool{
	return slices.Contains(numbers, value)
}

func Length() int{
	return len(numbers)
}

type Array struct{
	data []int
}

func NewArray() *Array{
	return &Array{
		data: []int{10,20,30},
	}
}

func (arr *Array) AddElem(value int)(){
	arr.data = append(arr.data, value)
}

func (arr *Array) IsExistElem(value int) bool {
	return slices.Contains(arr.data, value)
}

func (arr *Array) LengthArray() int{
	return len(arr.data)
}

func (arr *Array) PopElem() int {
	value:= arr.data[arr.LengthArray()-1]
	return value
}

