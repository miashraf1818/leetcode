
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # We have n + k - 1 total points after inserting k - 1 phantom points.
        # We need to choose exactly 2k points out of this expanded set.
        return math.comb(n + k - 1, 2 * k) % MOD