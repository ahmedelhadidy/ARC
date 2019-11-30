from src.Agent02 import *
import sys

json_file = '../data/training/0520fde7.json'
if len(sys.argv) > 1 :
    json_file = sys.argv[1]

explore_object = Agent02.explore(json_file)

for k,v in explore_object.items():
    for x in range(v):
        ag = Agent02(json_file,area=k,index=x)
        ag.solve()
        ag.print_spec()



