from NeuralNode import NeuralNode
import random


class NeuralLayer():
    def __init__(self, type, num_node, prev_num_node, init_weight=False):

        if not init_weight:
            self.nodes = [NeuralNode(type, [random.random() for node in range(0, prev_num_node)])
                          for x in range(0, num_node)]
        else:
            self.nodes = [NeuralNode(type, [init_weight[node] for node in range(0, prev_num_node)])
                          for x in range(0, num_node)]

    def caculate(self, inputs):
        """Caculate for layer

        Arguments:
            inputs {list} -- Previous input

        Returns:
            list -- list of result node
        """

        return [node.caculate(inputs) for node in self.nodes]
