from collections import defaultdict, deque
from typing import List

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        def topo(graph, indegree, nodes):
            q = deque()
            
            for node in nodes:
                if indegree[node] == 0:
                    q.append(node)

            order = []

            while q:
                node = q.popleft()
                order.append(node)

                for nei in graph[node]:
                    indegree[nei] -= 1

                    if indegree[nei] == 0:
                        q.append(nei)

            if len(order) != len(nodes):
                return []

            return order

        item_graph = defaultdict(list)
        item_indegree = [0] * n

        group_graph = defaultdict(list)
        group_indegree = [0] * m

        for item in range(n):
            for prev in beforeItems[item]:

                item_graph[prev].append(item)
                item_indegree[item] += 1

                g1 = group[prev]
                g2 = group[item]

                if g1 != g2:
                    group_graph[g1].append(g2)
                    group_indegree[g2] += 1

        group_order = topo(group_graph, group_indegree, list(range(m)))

        if not group_order:
            return []

        item_order = topo(item_graph, item_indegree, list(range(n)))

        if not item_order:
            return []

        grouped = defaultdict(list)

        for item in item_order:
            grouped[group[item]].append(item)

        ans = []

        for grp in group_order:
            ans.extend(grouped[grp])

        return ans