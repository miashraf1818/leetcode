import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        # dist[u][count] stores the minimum weight to reach node u 
        # with 'count' consecutive identical characters ending at u.
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        
        dist[0][1] = 0
        heap = [(0, 0, 1)] # (distance, node, count)
        
        while heap:
            d, u, count = heapq.heappop(heap)
            
            if d > dist[u][count]:
                continue
                
            if u == n - 1:
                return d
                
            ch_u = labels[u]
            for v, w in adj[u]:
                ch_v = labels[v]
                if ch_v == ch_u:
                    next_count = count + 1
                    if next_count <= k:
                        nd = d + w
                        if nd < dist[v][next_count]:
                            dist[v][next_count] = nd
                            heapq.heappush(heap, (nd, v, next_count))
                else:
                    nd = d + w
                    if nd < dist[v][1]:
                        dist[v][1] = nd
                        heapq.heappush(heap, (nd, v, 1))
                        
        return -1