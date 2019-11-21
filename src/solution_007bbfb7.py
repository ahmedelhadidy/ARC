from src.Agent01 import Agent01
import sys

json_file = '../data/training/007bbfb7.json'
if len(sys.argv) > 1 :
    json_file = sys.argv[1]

explore_object = Agent01.explore(json_file)

for k,v in explore_object.items():
    for x in range(v):
        ag = Agent01(json_file,area=k,index=x)
        ag.solve()
        ag.print()


