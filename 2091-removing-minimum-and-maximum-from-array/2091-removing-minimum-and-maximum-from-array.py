from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
            
        # Step 1: Find the indices of the minimum and maximum elements
        min_idx = 0
        max_idx = 0
        
        for i in range(1, n):
            if nums[i] < nums[min_idx]:
                min_idx = i
            elif nums[i] > nums[max_idx]:
                max_idx = i
                
        # Step 2: Assign the smaller index to `a` and larger to `b`
        a = min(min_idx, max_idx)
        b = max(min_idx, max_idx)
        
        # Step 3: Calculate the three possible deletion strategies
        both_from_front = b + 1
        both_from_back = n - a
        one_from_each_side = (a + 1) + (n - b)
        
        # Return the minimum deletions required
        return min(both_from_front, both_from_back, one_from_each_side)