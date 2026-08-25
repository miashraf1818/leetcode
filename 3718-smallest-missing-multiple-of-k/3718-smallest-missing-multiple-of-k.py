from typing import List

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num_set = set(nums)
        multiple = k
        
        # Increment by k until we find a multiple not in the set
        while multiple in num_set:
            multiple += k
            
        return multiple