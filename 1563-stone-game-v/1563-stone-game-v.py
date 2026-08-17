from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        if n <= 1:
            return 0
            
        # Prefix sum for O(1) subarray sum queries
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]
            
        # dp[i][j] = max score Alice can obtain from stoneValue[i..j]
        dp = [[0] * n for _ in range(n)]
        
        # max_l[i][j] caches max(dp[i][x] + sum(i, x)) for x in range [i..j]
        max_l = [[0] * n for _ in range(n)]
        # max_r[i][j] caches max(dp[x][j] + sum(x, j)) for x in range [i..j]
        max_r = [[0] * n for _ in range(n)]
        
        for i in range(n):
            max_l[i][i] = stoneValue[i]
            max_r[i][i] = stoneValue[i]
            
        # mid_x[i] dynamically tracks the maximum split point `m` where the 
        # left half's sum is <= the right half's sum as `j` extends to the right.
        mid_x = [i - 1 for i in range(n)]
        
        # Evaluate intervals by length to ensure dependencies are precalculated
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                total_sum = pref[j + 1] - pref[i]
                
                # Update moving boundary `m`
                m = mid_x[i]
                while m + 1 < j and 2 * (pref[m + 2] - pref[i]) <= total_sum:
                    m += 1
                mid_x[i] = m
                
                ans = 0
                
                # Evaluate choices bounded by the pivot `m`
                if m >= i:
                    ans = max(ans, max_l[i][m])
                
                if 2 * (pref[m + 1] - pref[i]) == total_sum:
                    # If perfectly equal at `m`, Alice can also freely elect the right side for `m`
                    if m + 1 <= j:
                        ans = max(ans, max_r[m + 1][j])
                else:
                    # Otherwise, Alice is restricted to right choices strictly after `m`
                    if m + 2 <= j:
                        ans = max(ans, max_r[m + 2][j])
                        
                dp[i][j] = ans
                
                # Update lookup tables for subsequent longer intervals
                max_l[i][j] = max(max_l[i][j - 1], ans + total_sum)
                max_r[i][j] = max(max_r[i + 1][j], ans + total_sum)
                
        return dp[0][n - 1]