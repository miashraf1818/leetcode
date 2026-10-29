import sys
from typing import List

sys.setrecursionlimit(200000)

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        parent = [0] * n
        depth = [0] * n
        size = [0] * n
        heavy = [-1] * n
        
        def dfs1(u, p, d):
            parent[u] = p
            depth[u] = d
            size[u] = 1
            max_sub = 0
            for v in adj[u]:
                if v != p:
                    dfs1(v, u, d + 1)
                    size[u] += size[v]
                    if size[v] > max_sub:
                        max_sub = size[v]
                        heavy[u] = v
                        
        dfs1(0, -1, 0)
        
        head = [0] * n
        pos = [0] * n
        cur_pos = 0
        
        def dfs2(u, h):
            nonlocal cur_pos
            head[u] = h
            pos[u] = cur_pos
            cur_pos += 1
            if heavy[u] != -1:
                dfs2(heavy[u], h)
            for v in adj[u]:
                if v != parent[u] and v != heavy[u]:
                    dfs2(v, v)
                    
        dfs2(0, 0)
        
        tree_vals = [0] * (4 * n)
        masks = [1 << (ord(ch) - ord('a')) for ch in s]
        
        def update_tree(node, l, r, idx, val):
            if l == r:
                tree_vals[node] = val
                return
            mid = (l + r) // 2
            if idx <= mid:
                update_tree(2 * node, l, mid, idx, val)
            else:
                update_tree(2 * node + 1, mid + 1, r, idx, val)
            tree_vals[node] = tree_vals[2 * node] ^ tree_vals[2 * node + 1]
            
        def query_tree(node, l, r, ql, qr):
            if qr < l or ql > r:
                return 0
            if ql <= l and r <= qr:
                return tree_vals[node]
            mid = (l + r) // 2
            return query_tree(2 * node, l, mid, ql, qr) ^ query_tree(2 * node + 1, mid + 1, r, ql, qr)

        for i in range(n):
            update_tree(1, 0, n - 1, pos[i], masks[i])
            
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                new_mask = 1 << (ord(c) - ord('a'))
                masks[u] = new_mask
                update_tree(1, 0, n - 1, pos[u], new_mask)
            else:
                u = int(parts[1])
                v = int(parts[2])
                path_xor = 0
                while head[u] != head[v]:
                    if depth[head[u]] < depth[head[v]]:
                        u, v = v, u
                    hu = head[u]
                    path_xor ^= query_tree(1, 0, n - 1, pos[hu], pos[u])
                    u = parent[hu]
                if depth[u] > depth[v]:
                    u, v = v, u
                path_xor ^= query_tree(1, 0, n - 1, pos[u], pos[v])
                
                if path_xor == 0 or (path_xor & (path_xor - 1)) == 0:
                    ans.append(True)
                else:
                    ans.append(False)
                    
        return ans