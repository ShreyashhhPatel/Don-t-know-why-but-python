from collections import defaultdict
import sys
from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        sys.setrecursionlimit(10**6)
        graph = defaultdict(list)

        ans = set()
        # building an adjenceny list




        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
            ans.add((min(u,v), max(u,v)))

        discovery_time = [-1] * n
        lowest_reachable_time = [0] * n
        current_time = [0]  # Use list to avoid global

        def dfs(u, parent):
            discovery_time[u] = current_time[0]    
            lowest_reachable_time[u] = current_time[0]
            current_time[0] += 1

            for v in graph[u]:
                if v == parent:
                    continue
                if discovery_time[v] == -1:
                    dfs(v, u)
                    lowest_reachable_time[u] = min(lowest_reachable_time[u], lowest_reachable_time[v])
                
                    if lowest_reachable_time[v] > discovery_time[u]:
                        ans.add((min(u,v), max(u,v)))
                    else:
                        ans.discard((min(u,v), max(u,v)))
                else:
                    # Back edge - part of a cycle, so NOT a bridge
                    lowest_reachable_time[u] = min(lowest_reachable_time[u], discovery_time[v])
                    ans.discard((min(u,v), max(u,v)))

        for node in range(n):
            if discovery_time[node] == -1:
                dfs(node, -1)

        return [list(edge) for edge in ans]


# Test the solution
if __name__ == "__main__":
    sol = Solution()
    n = 4
    connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
    result = sol.criticalConnections(n, connections)
    print("Critical connections:", result)        