from src.Agent02 import *

json_file = 'f:/personal/Master/Modules/Prog-tools/assignment3/solution/ARC/data/training/0520fde7.json'

explore_object = Agent02.explore(json_file)

for k,v in explore_object.items():
    for x in range(v):
        ag = Agent02(json_file,area=k,index=x)
        ag.solve()
        ag.print()



