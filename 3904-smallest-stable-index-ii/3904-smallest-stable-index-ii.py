class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        from typing import List

        n = len(nums)
        
        # Precompute the minimums from index i to the end of the array
        suf_min = [0] * n
        suf_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf_min[i] = min(nums[i], suf_min[i + 1])
            
        pref_max = float('-inf')
        
        # Iterate to find the smallest stable index in O(1) per step
        for i in range(n):
            if nums[i] > pref_max:
                pref_max = nums[i]
                
            instability_score = pref_max - suf_min[i]
            
            if instability_score <= k:
                return i
                
        return -1