from math import gcd
from typing import List

class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        n = len(nums)  # ← was missing!
        
        # Step 1: Build prefixGcd
        prefix_gcd = []
        max_so_far = 0
        for num in nums:
            max_so_far = max(max_so_far, num)
            prefix_gcd.append(gcd(num, max_so_far))
        
        # Step 2: Sort
        prefix_gcd.sort()
        
        # Step 3: Pair smallest with largest
        result = 0
        lo, hi = 0, n - 1
        while lo < hi:
            result += gcd(prefix_gcd[lo], prefix_gcd[hi])
            lo += 1
            hi -= 1
        
        return result