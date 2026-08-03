class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        
        # dp[i] = max score difference (current player - other player)
        # starting from index i
        # Same trick as "Predict the Winner"!
        
        dp = [float('-inf')] * (n + 1)
        dp[n] = 0  # no stones left → difference is 0
        
        # Suffix sum for quick range sum
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + stoneValue[i]
        
        for i in range(n - 1, -1, -1):
            for take in range(1, 4):  # take 1, 2, or 3 stones
                if i + take > n:
                    break
                # Score of taking stones[i..i+take-1] = suffix[i] - suffix[i+take]
                score = suffix[i] - suffix[i + take]
                # After taking, opponent plays from i+take
                # dp[i+take] is opponent's advantage, so we subtract it
                dp[i] = max(dp[i], score - dp[i + take])
        
        diff = dp[0]
        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        else:
            return "Tie"