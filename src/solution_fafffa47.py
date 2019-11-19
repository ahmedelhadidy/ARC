from src.Agent03 import *


json_file = 'f:/personal/Master/Modules/Prog-tools/assignment3/solution/ARC/data/training/fafffa47.json'
f = open(json_file, 'r')
ag = Agent03(f,use_train=False,train_index=3)
om = ag.solve()

print('=====','input','=====')
print(ag.input_matrix)
print('=====','original output','=====')
print(ag.output_matrix)
print('=====','calculated output','=====')
print(ag.calculated_output_matrix)
