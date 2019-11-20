from src.Agent01 import *


json_file = 'f:/personal/Master/Modules/Prog-tools/assignment3/solution/ARC/data/training/007bbfb7.json'

explore_object = Agent01.explore(json_file)

for k,v in explore_object.items():
    for x in range(v):
        ag = Agent01(json_file,area=k,index=x)
        ag.solve()
        ag.print()


