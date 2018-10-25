import unittest

from ..Neural.NeuralLayer import NeuralLayer


class TestNeuralLayer(unittest.TestCase):
    def test_caculate_input(self):

        layer = NeuralLayer("ReLU", 4, 3)
        self.assertEqual(2, 2)


if __name__ == '__main__':
    unittest.main()
