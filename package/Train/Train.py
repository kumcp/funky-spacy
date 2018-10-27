
class Train():

    def __init__(self, init_dataset, result_dataset, params):
        self.init_dataset = init_dataset
        self.result_dataset = result_dataset
        self.params = params

    def train(self, learning_rate):
        result = []
        for time in range(0, self.params.loop_time):

            result[time] = self.calculate(init_dataset[time])

    def calculate(self, inputs, network, param):
        pass
