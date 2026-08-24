from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        
        # Precompute the prefix sums
        pref = [0] * n
        pref[0] = stones[0]
        for i in range(1, n):
            pref[i] = pref[i - 1] + stones[i]
            
        # dp[n-1] is just pref[n-1] since taking the last index leaves 0 moves for the opponent
        ans = pref[-1]
        
        # Traverse backwards from the second-to-last choice down to the first available choice
        for i in range(n - 2, 0, -1):
            # We either take the current prefix sum minus the opponent's best future difference,
            # or we skip this index and keep the best difference we'd get from later indices.
            ans = max(ans, pref[i] - ans)
            
        return ans