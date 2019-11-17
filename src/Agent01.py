from src.ARC import *
import networkx as nx
import itertools


class Agent01(ARC):

    generators = {0:[0,1,2] , 1:[3,4,5] , 2:[6,7,8]}

    def __init__(self,f, use_train = False, train_index = 0):
        try:
            super(Agent01, self).__init__(f,use_train,train_index)
            self.validate_shape()
        except:
            print('Error ')

    def validate_shape(self):
        shape = self.input_matrix.shape
        if shape[0] != 3 or shape[0] != 3:
            raise Exception('input problem matrix is in invalid shape')

    def generate_output_matrix(self):
        # Replace zeros with 10
        self.input_matrix[self.input_matrix == 0] = 10
        input_graph = nx.from_numpy_matrix(self.input_matrix,create_using=nx.DiGraph())
        output_graph = nx.DiGraph()

        for s,d,w in input_graph.edges(data=True):
            if w['weight'] == 10:
                for x,y in itertools.product(self.generators[s] , self.generators[d]):
                    output_graph.add_edge(x,y,weight=10)
            else:
                for x, y in itertools.product(self.generators[s], self.generators[d]):
                    ox = self.generators[s].index(x)
                    oy = self.generators[d].index(y)
                    output_graph.add_edge(x, y, weight=input_graph[ox][oy]['weight'])

        self.calculated_output_matrix =  nx.to_numpy_array(output_graph,dtype=int)
        # replace 10 with zeros
        self.calculated_output_matrix[self.calculated_output_matrix == 10] = 0
        self.input_matrix[self.input_matrix == 10] = 0



