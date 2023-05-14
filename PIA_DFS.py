from inst15 import *

def dfs_complete_graph(assignments, values, kmin, kmax, dependencies={}):
    visited = set()
    stack = [(node, [node]) for node in assignments]
    shortest_path = None
    while stack:
        node, path = stack.pop()
        point_check(path,values,kmin,kmax)
        if point_check(path,values,kmin,kmax) == True:
                shortest_path = path
                return shortest_path
        elif node not in visited:
            visited.add(node)
            if node in dependencies:
                for dep_node in dependencies[node]:
                    if dep_node not in visited:
                        stack.pop()
                        stack.append((dep_node, [dep_node]))
                        visited.remove(node)
                        path.pop()
            for next_node in assignments:
                if next_node not in visited and next_node != node:
                    new_path = path + [next_node]
                    stack.append((next_node, new_path))
        else:
            shortest_path = path
            return shortest_path
    #return shortest_path

def point_check(curr_path, values, kmin, kmax):
    points = 0
    for node in curr_path:
        if node in values:
            points += values[node]
    if points >= kmin and points <= kmax:
        return True
    else:
        return False

required = []
dependencies = {}
kmin = 300
kmax = 800

shortest_path = dfs_complete_graph(assignments, values, kmin, kmax, dependencies)

print(shortest_path)
total = 0
total2 = 0
for node in shortest_path:
    if node in times:
        total += times[node]
    if node in values:
        total2 += values[node]
print("Tiempo: "+str(total))
print("Valores: "+str(total2))

"""
if set(required).issubset(set(shortest_path)):
    print(shortest_path)
    total = 0
    total2 = 0
    for node in shortest_path:
        if node in times:
            total += times[node]
        if node in values:
            total2 += values[node]
    print("Tiempo: "+str(total))
    print("Valores: "+str(total2))
else:
    shortest_path0 = [item for item in shortest_path if item not in required]
    shortest_path2 = required + shortest_path0
    print(shortest_path2)
    total = 0
    total2 = 0
    for node in shortest_path2:
        if node in times:
            total += times[node]
        if node in values:
            total2 += values[node]
    print("Tiempo: "+str(total))
    print("Valores: "+str(total2))
"""
