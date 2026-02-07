# frag7_parent.py
from collections import defaultdict

n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]

graph = defaultdict(list)
for a, b in connections:
    graph[a].append(b)
    graph[b].append(a)

disc = [-1] * n
time = 0

def dfs(u, parent):
    global time
    disc[u] = time
    print(f"Visit {u}, parent={parent}, disc={time}")
    time += 1

    for v in graph[u]:
        print(v, "-->", u)
        if v == parent:
            print(f"  Skip parent edge {u}->{v}")
            continue
        if disc[v] == -1:
            dfs(v, u)
        print(v,u)

dfs(0, -1)
