from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # Precompute suffix sums to quickly get total stones remaining from any index
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        memo = {}
        
        def dp(i: int, m: int) -> int:
            # If all piles have been taken
            if i >= n:
                return 0
                
            # If the current player has a large enough M to take all remaining piles, they should take them all
            if i + 2 * m >= n:
                return suffix_sum[i]
                
            if (i, m) in memo:
                return memo[(i, m)]
                
            max_stones = 0
            
            # The player can take X piles, where 1 <= X <= 2M
            for x in range(1, 2 * m + 1):
                # The current player gets all remaining stones minus what the next player optimally secures
                current_stones = suffix_sum[i] - dp(i + x, max(m, x))
                max_stones = max(max_stones, current_stones)
                
            memo[(i, m)] = max_stones
            return max_stones
            
        # Alice goes first starting at index 0 with M = 1
        return dp(0, 1)