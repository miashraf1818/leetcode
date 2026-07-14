from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        MAX_VAL = 201

        # dp[g1][g2] = number of ways to pick (seq1, seq2) where
        # gcd(seq1) = g1, gcd(seq2) = g2, using elements considered so far
        # g1=0 or g2=0 means that subsequence is empty so far
        dp = [[0] * MAX_VAL for _ in range(MAX_VAL)]
        dp[0][0] = 1  # base: both subsequences empty

        for num in nums:
            # Traverse in reverse to avoid using same num twice
            new_dp = [[0] * MAX_VAL for _ in range(MAX_VAL)]
            for g1 in range(MAX_VAL):
                for g2 in range(MAX_VAL):
                    if dp[g1][g2] == 0:
                        continue
                    ways = dp[g1][g2]

                    # Option 1: skip num (don't add to either)
                    new_dp[g1][g2] = (new_dp[g1][g2] + ways) % MOD

                    # Option 2: add num to seq1
                    ng1 = gcd(g1, num) if g1 != 0 else num
                    new_dp[ng1][g2] = (new_dp[ng1][g2] + ways) % MOD

                    # Option 3: add num to seq2
                    ng2 = gcd(g2, num) if g2 != 0 else num
                    new_dp[g1][ng2] = (new_dp[g1][ng2] + ways) % MOD

            dp = new_dp

        # Sum all pairs where g1 == g2 and both non-zero
        result = 0
        for g in range(1, MAX_VAL):
            result = (result + dp[g][g]) % MOD

        return result