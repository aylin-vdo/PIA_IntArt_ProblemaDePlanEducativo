from inst15 import *

def bfs_complete_graph(assignments, times, kmin, kmax, dependencies={}):
    sorted_list = []
    for node in assignments:
        if point_check(sorted_list,values,kmin,kmax) == True:
            break
        if node not in sorted_list:
            added = False
            for i in range(len(sorted_list)):
                if node in dependencies.get(sorted_list[i], []):
                    sorted_list.insert(i, node)
                    added = True
                    break
                elif times[node] < times[sorted_list[i]]:
                    sorted_list.insert(i, node)
                    added = True
                    break
            if not added:
                sorted_list.append(node)
    return sorted_list

def point_check(curr_path, values, kmin, kmax):
    points = 0
    for node in curr_path:
        if node in values:
            points += values[node]
    if points >= kmin and points <= kmax:
        return True
    else:
        return False


kmin = 300
kmax = 800

shortest_path = bfs_complete_graph(assignments, values, kmin, kmax, dependencies)

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

# Maneja si tiene actividades requeridas/obligatorias
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
