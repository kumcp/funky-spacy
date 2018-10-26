import unittest

from ..Neural.NeuralLayer import NeuralLayer


class TestNeuralLayer(unittest.TestCase):
    def test_caculate_input(self):

        layer = NeuralLayer("sigmoid", 4, 3)
        print(layer.nodes)
        print(layer.caculate([9999, 99999, 99999]))
        self.assertEqual(2, 2)


if __name__ == '__main__':
    unittest.main()
