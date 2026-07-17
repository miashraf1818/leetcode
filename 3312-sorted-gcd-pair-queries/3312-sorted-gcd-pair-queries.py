from math import gcd
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        MOD_VAL = max(nums)
        
        freq = [0] * (MOD_VAL + 1)
        for num in nums:
            freq[num] += 1
        
        div_count = [0] * (MOD_VAL + 1)
        for g in range(1, MOD_VAL + 1):
            total = 0
            for multiple in range(g, MOD_VAL + 1, g):
                total += freq[multiple]
            div_count[g] = total * (total - 1) // 2

        exact = [0] * (MOD_VAL + 1)
        for g in range(MOD_VAL, 0, -1):
            exact[g] = div_count[g]
            for multiple in range(2 * g, MOD_VAL + 1, g):
                exact[g] -= exact[multiple]
        
        prefix = [0] * (MOD_VAL + 2)
        for g in range(1, MOD_VAL + 1):
            prefix[g] = prefix[g - 1] + exact[g]
        
        result = []
        for q in queries:
            lo, hi = 1, MOD_VAL
            while lo < hi:
                mid = (lo + hi) // 2
                if prefix[mid] > q:
                    hi = mid
                else:
                    lo = mid + 1
            result.append(lo)
        
        return result