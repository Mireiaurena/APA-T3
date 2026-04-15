"""
Módulo vectores.py para la gestión de operaciones con vectores.
Alumno: Mireia Ureña López

Tests unitarios:
>>> v1 = Vector([1, 2, 3])
>>> v2 = Vector([4, 5, 6])
>>> v1 * 2
Vector([2, 4, 6])
>>> v1 * v2
Vector([4, 10, 18])
>>> v1 @ v2
32
>>> v1 = Vector([2, 1, 2])
>>> v2 = Vector([0.5, 1, 0.5])
>>> v1 // v2
Vector([1.0, 2.0, 1.0])
>>> v1 % v2
Vector([1.0, -1.0, 1.0])
"""

class Vector:
    """Clase para representar vectores euclidianos y realizar operaciones de álgebra lineal."""

    def __init__(self, componentes):
        """Inicializa una instancia de Vector a partir de una secuencia de componentes numéricas."""
        self.vector = list(componentes)

    def __repr__(self):
        """Devuelve una cadena de texto que representa formalmente al objeto Vector."""
        return f"Vector({self.vector})"

    def __add__(self, otro):
        """Retorna un nuevo Vector tras sumar elemento a elemento los componentes de ambos operandos."""
        return Vector(a + b for a, b in zip(self.vector, otro.vector))

    def __sub__(self, otro):
        """Retorna un nuevo Vector tras restar elemento a elemento los componentes de ambos operandos."""
        return Vector(a - b for a, b in zip(self.vector, otro.vector))

    def __mul__(self, otro):
        """Realiza el producto de Hadamard si el argumento es un Vector o escala los componentes si es un número."""
        if isinstance(otro, (int, float)):
            return Vector(a * otro for a in self.vector)
        elif isinstance(otro, Vector):
            return Vector(a * b for a, b in zip(self.vector, otro.vector))
        return NotImplemented

    def __rmul__(self, otro):
        """Permite realizar la multiplicación por un escalar cuando este aparece a la izquierda del vector."""
        return self.__mul__(otro)

    def __matmul__(self, otro):
        """Calcula y devuelve el producto escalar (dot product) entre dos vectores mediante el operador @."""
        return sum(a * b for a, b in zip(self.vector, otro.vector))

    def __floordiv__(self, otro):
        """Calcula la componente tangencial (proyección paralela) de este vector sobre el argumento usando el operador //."""
        proyeccion = (self @ otro) / (otro @ otro)
        return proyeccion * otro

    def __mod__(self, otro):
        """Calcula la componente normal (proyección perpendicular) de este vector respecto al argumento usando el operador %."""
        return self - (self // otro)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

    