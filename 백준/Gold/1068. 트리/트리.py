# 트리
from collections import defaultdict

n = int(input())
parents = list(map(int, input().split()))
delete = int(input())

nodes = defaultdict(list)
count = 0

for i, p in enumerate(parents):
    # {node : parent}
    nodes[p].append(i)
    
def deleteNode(delNode):
    child = []
    if delNode in nodes.keys():
        child = nodes[delNode]
        # remove parent
        del nodes[delNode]

    # remove child
    for node in nodes:
        if delNode in nodes[node]:
            nodes[node].remove(delNode)
            
    # remove All child node of delNode (chain rule)
    if child:
        for c in child:
            deleteNode(c)
           
deleteNode(delete)
values = []
for x in nodes.values():
    values.extend(x)
    

for i in values:
    if nodes[i] == []:
            count += 1
        
print(count)