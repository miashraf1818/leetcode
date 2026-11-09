import heapq
from typing import List
from sortedcontainers import SortedSet

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = SortedSet(range(k))
        busy = []  # stores tuples of (free_time, server_id)
        request_count = [0] * k
        
        for i in range(len(arrival)):
            arr_time = arrival[i]
            duration = load[i]
            
            # Free up servers that have completed their tasks by arr_time
            while busy and busy[0][0] <= arr_time:
                _, server_id = heapq.heappop(busy)
                available.add(server_id)
                
            if not available:
                continue  # All servers are busy, drop the request
                
            pref = i % k
            idx = available.bisect_left(pref)
            if idx == len(available):
                server_id = available[0]
            else:
                server_id = available[idx]
                
            available.remove(server_id)
            request_count[server_id] += 1
            heapq.heappush(busy, (arr_time + duration, server_id))
            
        max_requests = max(request_count)
        return [i for i, count in enumerate(request_count) if count == max_requests]