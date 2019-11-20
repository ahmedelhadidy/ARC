from src.ARC import *
import networkx as nx


class Agent02(ARC):

    def generate_output_matrix(self):
        M1 = self.input_matrix[:, 0:3]
        M2 = self.input_matrix[:, 4:7]

        G1 = nx.from_numpy_matrix(M1, create_using=nx.DiGraph())
        G2 = nx.from_numpy_matrix(M2, create_using=nx.DiGraph())
        OG = nx.intersection(G1, G2)
        output_matrix = nx.to_numpy_array(OG, dtype=int)

        output_matrix[output_matrix !=0] = 2
        return output_matrix


