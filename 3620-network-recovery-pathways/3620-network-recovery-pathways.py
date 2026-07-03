import heapq
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        
        graph = [[] for _ in range(n)]
        for u, v, cost in edges:
            graph[u].append((v, cost))
        
        def canAchieve(minEdge):
            dist = [float('inf')] * n
            dist[0] = 0
            heap = [(0, 0)]
            
            while heap:
                cost_so_far, node = heapq.heappop(heap)
                
                if cost_so_far > dist[node]:
                    continue
                
                if node == n - 1:
                    return cost_so_far <= k
                
                for nei, edge_cost in graph[node]:
                    if edge_cost < minEdge:
                        continue
                    if nei != n - 1 and not online[nei]:
                        continue
                    new_cost = cost_so_far + edge_cost
                    if new_cost < dist[nei]:
                        dist[nei] = new_cost
                        heapq.heappush(heap, (new_cost, nei))
            
            return False
        
        candidates = sorted(set(cost for _, _, cost in edges))  # ascending!
        
        if not candidates:
            return -1
        
        lo, hi = 0, len(candidates) - 1
        result = -1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if canAchieve(candidates[mid]):
                result = candidates[mid]
                lo = mid + 1
            else:
                hi = mid - 1
        
        return result