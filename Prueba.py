# file: test_operations.py
import unittest
from operations import X


class TestOperations(unittest.TestCase):

    def setUp(self):
        self.calculadora = X()

    def test_sumar(self):
        self.assertEqual(self.calculadora.sumar(5, 3), 8)
        self.assertEqual(self.calculadora.sumar(-1, 1), 0)

    def test_restar(self):
        self.assertEqual(self.calculadora.restar(10, 5), 5)
        self.assertEqual(self.calculadora.restar(0, 5), -5)


if __name__ == '__main__':
    unittest.main()

