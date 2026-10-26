from typing import List
from collections import deque

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    total = 0
                    queue = deque([(r, c)])
                    total += grid[r][c]
                    grid[r][c] = 0
                    
                    while queue:
                        curr_r, curr_c = queue.popleft()
                        for nr, nc in ((curr_r + 1, curr_c), (curr_r - 1, curr_c), (curr_r, curr_c + 1), (curr_r, curr_c - 1)):
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                total += grid[nr][nc]
                                grid[nr][nc] = 0
                                queue.append((nr, nc))
                                
                    if total % k == 0:
                        ans += 1
                        
        return ans