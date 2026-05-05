class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)

        # Build graph
        graph = [[] for _ in range(n)]

        for i in range(n):
            x1, y1, r1 = bombs[i]

            for j in range(n):
                if i == j:
                    continue

                x2, y2, _ = bombs[j]

                # Distance squared
                dx = x1 - x2
                dy = y1 - y2

                # If bomb j is inside bomb i's range
                if dx * dx + dy * dy <= r1 * r1:
                    graph[i].append(j)

        # DFS to count detonations
        def dfs(node, visited):
            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei, visited)

            return len(visited)

        ans = 0

        for i in range(n):
            visited = set()
            ans = max(ans, dfs(i, visited))

        return ans