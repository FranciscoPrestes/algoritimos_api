import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.computed_property import ComputedProperty


class Dummy:
    def __init__(self, x: int):
        self._x = x

    @ComputedProperty('_x')
    def double(self):
        """
        Propriedade computada que retorna o dobro de _x.
        """
        return self._x * 2

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value


class TestComputedProperty(unittest.TestCase):

    def test_property_cache_update(self):
        """
        Testa se a propriedade computada atualiza o cache corretamente.
        """
        # Arrange
        dummy = Dummy(5)

        # Act
        result_initial = dummy.double
        dummy.x = 10
        result_updated = dummy.double

        # Assert
        self.assertEqual(result_initial, 10)
        self.assertEqual(result_updated, 20)

    def test_no_dependencies(self):
        """
        Testa se a ausência de dependências gera ValueError.
        """
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            ComputedProperty()  # agora levanta ValueError na ausência de dependências


if __name__ == "__main__":
    unittest.main()
