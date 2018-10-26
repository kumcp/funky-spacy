import unittest

from ..Neural.NeuralLayer import NeuralLayer
from ..Neural.NeuralNode import NeuralNodeType


class TestNeuralLayer(unittest.TestCase):
    def test_caculate_input(self):

        layer = NeuralLayer(NeuralNodeType.SIGMOID, 4, 3)
        print(layer.nodes)
        print(layer.caculate([-0.2, 0.5, -0.3]))
        self.assertEqual(2, 2)


if __name__ == '__main__':
    unittest.main()
