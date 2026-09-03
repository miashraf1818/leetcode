class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        from typing import List

        min_val = min(nums1)
        
        # If the absolute minimum is odd, it can be used to convert all even numbers to odd.
        if min_val % 2 != 0:
            return True
            
        # If the minimum is even, a valid array is only possible if NO odd numbers exist at all.
        return all(x % 2 == 0 for x in nums1)