
import math
from enum import Enum


def func_sigmoid(x, derivate=False):
    sig = 1 / (1 + math.exp(x))
    if derivate:
        return sig * (1 - sig)
    return sig


def func_relu(x, derivate=False):
    if derivate:
        return 1 if x > 0 else 0
    return x if x > 0 else 0


class NeuralNodeType(Enum):
    SIGMOID = "sigmoid"
    RELU = "ReLU"


class NeuralNode():

    def __init__(self, type, init_weight):
        """Constructor a node

        Arguments:
            type {NeuralNodeType} -- Using type of caculate in NeuralNodeType
            init_weight {list} -- weight values
        """

        self.weight = init_weight
        self.type = type

    def update_weight(self, lambda_weight):
        """Update weight with lambda weight

        Arguments:
            lambda_weight {list} -- weight changes

        Raises:
            ValueError -- raise if length of lambda_weight and weight is not equal
        """

        if len(self.weight) != len(lambda_weight):
            raise ValueError("Length of weight and lambda weight is not equal")

        self.weight = [(x + y) for x, y in zip(self.weight, lambda_weight)]

    def caculate(self, inputs):
        return {
            NeuralNodeType.SIGMOID: func_sigmoid,
            NeuralNodeType.RELU: func_relu
        }[self.type](self.convolution(inputs))

    def convolution(self, inputs):

        if len(self.weight) != len(inputs):
            raise ValueError("Length of weight and lambda weight is not equal")

        return sum([(x * y) for x, y in zip(self.weight, inputs)])


test = NeuralNode(NeuralNodeType.RELU, [1, 5, 6])
test.update_weight([2, -6, -4])

print(test.caculate([2, 5, 7]))
