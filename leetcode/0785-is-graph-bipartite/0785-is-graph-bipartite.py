from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n
        for start in range(n):
            if color[start] != 0:
                continue
            queue = deque([start])
            color[start] = 1
            while queue:
                node = queue.popleft()
                for neighbour in graph[node]:
                    if color[neighbour] == 0:
                        color[neighbour] = -color[node]
                        queue.append(neighbour)
                    elif color[neighbour] == color[node]:
                        return False
        return True


        

        
       