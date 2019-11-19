from src.ARC import *
import networkx as nx
from networkx.algorithms.operators.binary import compose



class Agent03(ARC):

    def generate_output_matrix(self):
        M1 = self.input_matrix[0:3, :]
        M2 = self.input_matrix[3:6, :]

        G1 = nx.from_numpy_matrix(M1, create_using=nx.DiGraph())
        G2 = nx.from_numpy_matrix(M2, create_using=nx.DiGraph())
        OG = compose(G1, G2)
        self.calculated_output_matrix = nx.to_numpy_array(OG, dtype=int)

        self.calculated_output_matrix[self.calculated_output_matrix == 0] = 2
        self.calculated_output_matrix[self.calculated_output_matrix != 2] = 0

        return self.calculated_output_matrix