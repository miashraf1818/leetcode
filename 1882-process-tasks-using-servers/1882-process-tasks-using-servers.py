import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        n = len(servers)
        m = len(tasks)
        
        # Free servers heap: stores tuples of (weight, index)
        free_servers = [(servers[i], i) for i in range(n)]
        heapq.heapify(free_servers)
        
        # Busy servers heap: stores tuples of (free_time, weight, index)
        busy_servers = []
        
        ans = [0] * m
        current_time = 0
        
        for j in range(m):
            current_time = max(current_time, j)
            
            # Free up servers whose tasks are completed by current_time
            while busy_servers and busy_servers[0][0] <= current_time:
                free_time, weight, index = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, index))
                
            # If no free servers are available, jump time to the next available server
            if not free_servers:
                current_time = busy_servers[0][0]
                while busy_servers and busy_servers[0][0] <= current_time:
                    free_time, weight, index = heapq.heappop(busy_servers)
                    heapq.heappush(free_servers, (weight, index))
                    
            # Assign the task to the best available server
            weight, index = heapq.heappop(free_servers)
            ans[j] = index
            heapq.heappush(busy_servers, (current_time + tasks[j], weight, index))
            
        return ans