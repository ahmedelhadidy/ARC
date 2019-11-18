from src.Agent02 import *


json_file = 'f:/personal/Master/Modules/Prog-tools/assignment3/solution/ARC/data/training/0520fde7.json'
f = open(json_file, 'r')
ag = Agent02(f)
om = ag.solve()

print('=====','input','=====')
print(ag.input_matrix)
print('=====','original output','=====')
print(ag.output_matrix)
print('=====','calculated output','=====')
print(ag.calculated_output_matrix)
