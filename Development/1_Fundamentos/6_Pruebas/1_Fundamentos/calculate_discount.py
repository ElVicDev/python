# Escenario real: Un ejemplo sencillo

""" Supongamos que estás creando una aplicación de calculadora en Python. 
    Tienes una función llamada calculate_discount(price, percentage) que 
    calcula el precio con descuento. 
    Aquí tienes una sencilla prueba unitaria para esta función utilizando 
    el módulo pytest integrado en Python: """

import pytest 
def calculate_discount(price, percentage):
    return price - (price * percentage / 100)

class TestDiscountCalculation:
    def test_ten_percent_discount(self):
        result = calculate_discount(100, 10)
        assert result == 90  # Assertion

    def test_invalid_input(self):
        with pytest.raises(TypeError):
            calculate_discount("100", 10)   # Test for incorrect input type

""" Las pruebas unitarias no son simplemente una casilla a marcar; 
    es una habilidad fundamental que te permite crear aplicaciones Python 
    más robustas y fiables. 
    Descomponiendo tu código, anticipando su comportamiento y probando 
    meticulosamente cada unidad, ganarás confianza para refactorizar y 
    expandir tus proyectos sin miedo.  """