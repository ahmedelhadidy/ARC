from src.ARC import *
import networkx as nx
import itertools


class Agent01(ARC):

    generators = {0:[0,1,2] , 1:[3,4,5] , 2:[6,7,8]}

    def generate_output_matrix(self):
        input_mtx = self.input_matrix.copy()
        # Replace zeros with 10
        input_mtx[input_mtx == 0] = 10
        input_graph = nx.from_numpy_matrix(input_mtx,create_using=nx.DiGraph())
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

        output_matrix =  nx.to_numpy_array(output_graph,dtype=int)
        # replace 10 with zeros
        output_matrix[output_matrix == 10] = 0

        return output_matrix



