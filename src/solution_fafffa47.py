from src.Agent03 import *

json_file = 'f:/personal/Master/Modules/Prog-tools/assignment3/solution/ARC/data/training/fafffa47.json'
explore_object = Agent03.explore(json_file)
for k,v in explore_object.items():
    for x in range(v):
        ag = Agent03(json_file,area=k,index=x)
        ag.solve()
        ag.print()
