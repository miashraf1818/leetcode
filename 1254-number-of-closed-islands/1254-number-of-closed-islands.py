from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C:
                return False
            if grid[r][c] == 1:
                return True
            grid[r][c] = 1
            
            res = True
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if not dfs(nr, nc):
                    res = False
            return res

        ans = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    if dfs(r, c):
                        ans += 1
        return ans
        