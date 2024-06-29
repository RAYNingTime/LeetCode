class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            reverse_graph[v].append(u)
        
        indegree = [0] * n
        for u in range(n):
            for v in graph[u]:
                indegree[v] += 1
        
        queue = deque([i for i in range(n) if indegree[i] == 0])
        topo_order = []
        
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        ancestors = [set() for _ in range(n)]
        
        for node in topo_order:
            for parent in reverse_graph[node]:
                ancestors[node].add(parent)
                ancestors[node].update(ancestors[parent])
        
        answer = [sorted(list(ancestor_set)) for ancestor_set in ancestors]
        
        return answer
