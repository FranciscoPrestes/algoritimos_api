import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.computed_property import ComputedProperty

class Example:
    def __init__(self, x: int = 0):
        self._x = x

    @ComputedProperty('x')
    def double(self):
        """
        Propriedade computada que retorna o dobro de x.

        Returns:
            int: O valor de x * 2.
        """
        return self._x * 2

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

if __name__ == "__main__":
    """
    Script de exemplo para testar a ComputedProperty.
    """
    example = Example(5)
    print(f"Double inicial: {example.double}")
    example.x = 10
    print(f"Double atualizado: {example.double}")
