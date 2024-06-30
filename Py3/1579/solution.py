class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf_alice = UnionFind(n)
        uf_bob = UnionFind(n)
        uf_combined = UnionFind(n)
        
        used_edges = 0
        
        # Sort edges by type to handle type 3 edges first
        edges.sort(reverse=True, key=lambda x: x[0])
        
        for edge in edges:
            t, u, v = edge
            u -= 1  # Adjust for 0-based index
            v -= 1
            
            if t == 3:
                if uf_combined.union(u, v):
                    used_edges += 1
                    uf_alice.union(u, v)
                    uf_bob.union(u, v)
            elif t == 1:
                if uf_alice.union(u, v):
                    used_edges += 1
            elif t == 2:
                if uf_bob.union(u, v):
                    used_edges += 1
        
        # Check if both Alice and Bob can traverse the entire graph
        if len({uf_alice.find(x) for x in range(n)}) > 1 or len({uf_bob.find(x) for x in range(n)}) > 1:
            return -1
        
        return len(edges) - used_edges
