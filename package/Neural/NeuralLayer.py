from NeuralNode import NeuralNode


class NeuralLayer():
    def __init__(self, type, num_node, prev_num_node):
        self.nodes = [NeuralNode(type, [0 for x in range(0, prev_num_node)])
                      for x in range(0, num_node)]

    def caculate(self, inputs):
        return [node.caculate(inputs) for node in self.nodes]
