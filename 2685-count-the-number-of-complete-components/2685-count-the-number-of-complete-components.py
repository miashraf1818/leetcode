class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Union-Find
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1

        for a, b in edges:
            union(a, b)

        # Count nodes and edges per component
        from collections import defaultdict
        node_count = defaultdict(int)
        edge_count = defaultdict(int)

        for i in range(n):
            node_count[find(i)] += 1

        for a, b in edges:
            edge_count[find(a)] += 1

        # A complete component with k nodes needs exactly k*(k-1)/2 edges
        result = 0
        for root in node_count:
            k = node_count[root]
            if edge_count[root] == k * (k - 1) // 2:
                result += 1

        return result