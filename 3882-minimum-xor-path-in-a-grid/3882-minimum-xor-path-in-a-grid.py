from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [set() for _ in range(n)]
        
        dp[0].add(grid[0][0])
        for c in range(1, n):
            dp[c] = {x ^ grid[0][c] for x in dp[c-1]}
            
        for r in range(1, m):
            new_dp = [set() for _ in range(n)]
            new_dp[0] = {x ^ grid[r][0] for x in dp[0]}
            for c in range(1, n):
                vals = dp[c].union(new_dp[c-1])
                new_dp[c] = {x ^ grid[r][c] for x in vals}
            dp = new_dp
            
        return min(dp[-1])