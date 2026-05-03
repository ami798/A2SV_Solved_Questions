from collections import defaultdict, deque
from typing import List

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = defaultdict(list)
        indegree = [0] * (n + 1)
        
        
        for u, v in relations:
            adj[u].append(v)
            indegree[v] += 1
        
        
        dp = [0] * (n + 1)
        
        q = deque()
        
        
        for i in range(1, n + 1):
            dp[i] = time[i - 1]
            if indegree[i] == 0:
                q.append(i)
        
        
        while q:
            u = q.popleft()
            
            for v in adj[u]:
               
                dp[v] = max(dp[v], dp[u] + time[v - 1])
                
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        
        return max(dp)