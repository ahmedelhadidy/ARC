from src.Agent03 import *
import sys

json_file = '../data/training/fafffa47.json'
if len(sys.argv) > 1 :
    json_file = sys.argv[1]

explore_object = Agent03.explore(json_file)
for k,v in explore_object.items():
    for x in range(v):
        ag = Agent03(json_file,area=k,index=x)
        ag.solve()
        ag.print()
