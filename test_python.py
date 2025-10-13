from algoritmia import factorial

class TestAlgotitmos():
    def test_factorial_potitivo(self):
        assert factorial(5) == 120
    
    def test_factorial_negativo(self):
        assert factorial(-5) == 0