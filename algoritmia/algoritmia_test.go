package algoritmia

import "testing"

func TestFactorialPositivo(t *testing.T)  {
	result:= Factorial(5)
	esperado:=120
	if result != esperado{
		t.Errorf("Factorial(5)=%d, esperado=%d", result, esperado)
	}
}

func TestFactorialNegativos(t *testing.T)  {
	result:= Factorial(-5)
	esperado:=0
	if result != esperado{
		t.Errorf("Factorial(-5)=%d, esperado=%d", result, esperado)
	}
}