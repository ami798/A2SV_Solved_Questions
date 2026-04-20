from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[]for _ in range(n)]
        for u,v in edges:
            graph[v].append(u)
            graph[u].append(v)
        visited = set()
        def check(node):
            if node == destination:
                return True
            if node in visited:
                return False
            visited.add(node)
            for nei in graph[node]:
                if check(nei):
                    return True
            return False
        return check(source)

