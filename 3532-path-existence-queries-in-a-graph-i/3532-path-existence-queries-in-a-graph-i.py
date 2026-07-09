class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # Build Union-Find
        parent = list(range(n))
        rank = [0] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression
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
        
        # Since nums is sorted, only check adjacent nodes!
        for i in range(n - 1):
            if nums[i+1] - nums[i] <= maxDiff:
                union(i, i + 1)
        
        # Answer each query in O(1)
        return [find(u) == find(v) for u, v in queries]