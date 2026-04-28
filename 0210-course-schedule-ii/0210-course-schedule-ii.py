from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for d,src in prerequisites:
            graph[src].append(d)
        visited = [0] *numCourses
        order = []
        def dfs(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True
            visited[node] = 1
            for neighbour in graph[node]:
                if not dfs(neighbour): return False
            visited[node] = 2
            order.append(node)
            return True
        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return []
        return order[::-1]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # graph = [[] for _ in range(numCourses)]
        # indegree = [0] * numCourses
        # for d,src in prerequisites:
        #     graph[src].append(d)
        #     indegree[d] += 1
        # queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        # order = []
        # while queue:
        #     node = queue.popleft()
        #     order.append(node)
        #     for neighbour in graph[node]:
        #         indegree[neighbour] -= 1
        #         if indegree[neighbour] == 0:
        #             queue.append(neighbour)
        # return order if len(order) == numCourses else []
          