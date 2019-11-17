import json
import numpy as np

class ARC:

    input_matrix  = None
    output_matrix = None
    calculated_output_matrix = None

    def __init__(self, f, use_train = False, train_index = 0):
        js = json.load(f)
        if use_train:
            self.input_matrix = np.matrix(js['train'][train_index]['input'])
            self.output_matrix = np.matrix(js['train'][train_index]['output'])
        else:
            self.input_matrix = np.matrix(js['test'][0]['input'])
            self.output_matrix = np.matrix(js['test'][0]['output'])

    def solve(self):
        generated_matrix = self.generate_output_matrix()
        return generated_matrix;

    def generate_output_matrix(self):
        pass

