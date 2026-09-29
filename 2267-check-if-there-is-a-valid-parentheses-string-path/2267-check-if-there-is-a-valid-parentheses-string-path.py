from typing import List
from functools import cache

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        if (m + n) % 2 == 0 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
            
        max_bal = (m + n - 1) // 2
        
        @cache
        def dfs(r: int, c: int, bal: int) -> bool:
            bal += 1 if grid[r][c] == '(' else -1
            
            if bal < 0 or bal > max_bal:
                return False
                
            if r == m - 1 and c == n - 1:
                return bal == 0
                
            if r + 1 < m and dfs(r + 1, c, bal):
                return True
            if c + 1 < n and dfs(r, c + 1, bal):
                return True
                
            return False
            
        return dfs(0, 0, 0)