from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda l: l[1])
        indexed_queries = sorted(enumerate(queries), key=lambda q: q[1])
        
        ans = [0] * len(queries)
        counts = {}
        
        left = 0
        right = 0
        l_len = len(logs)
        
        for q_idx, q_time in indexed_queries:
            start = q_time - x
            end = q_time
            
            while right < l_len and logs[right][1] <= end:
                server_id = logs[right][0]
                counts[server_id] = counts.get(server_id, 0) + 1
                right += 1
                
            while left < l_len and logs[left][1] < start:
                server_id = logs[left][0]
                counts[server_id] -= 1
                if counts[server_id] == 0:
                    del counts[server_id]
                left += 1
                
            ans[q_idx] = n - len(counts)
            
        return ans