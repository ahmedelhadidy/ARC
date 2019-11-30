import json
import numpy as np
import os as os


class ARC:

    input_matrix  = None
    original_output_matrix = None
    calculated_output_matrix = None
    file_name = None

    def __init__(self, file, area='train', index = 0):
        f = open(file, 'r')
        try:
            js = json.load(f)
            self.file_name = os.path.basename(f.name)
            self.input_matrix = np.matrix(js[area][index]['input'])
            self.original_output_matrix = np.matrix(js[area][index]['output'])
            self.area = area
            self.area_index = index
            f.close()
        finally:
            f.close()

    def solve(self):
        self.calculated_output_matrix = self.generate_output_matrix()
        return self.calculated_output_matrix;

    def print(self):
        print('=====',self.file_name,self.area,self.area_index+1,'=====')
        print('=====', 'input', '=====')
        print(self.input_matrix)
        print('=====', 'original output', '=====')
        print(self.original_output_matrix)
        print('=====', 'calculated output', '=====')
        print(self.calculated_output_matrix)

    def print_spec(self):
        for in_lst in np.squeeze(np.asarray(self.input_matrix)):
            print(' '.join(map(str,in_lst)))
        print(' ')
        for out_lst in self.calculated_output_matrix:
            print(' '.join(map(str,out_lst)))
        print(' ')

    def generate_output_matrix(self):
        pass

    def explore(file):
        f = open(file, 'r')
        try:
            js = json.load(f)
            train_cases_count = len(js['train'])
            test_cases_count = len(js['test'])
            f.close()
            return {'train': train_cases_count, 'test': test_cases_count}
        finally:
            f.close()



