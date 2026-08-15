from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0
        has_nonzero = False
        
        # Calculate total XOR and check if there are any non-zero elements
        for num in nums:
            total_xor ^= num
            if num != 0:
                has_nonzero = True
                
        # Case 3: The array is entirely zeroes
        if not has_nonzero:
            return 0
            
        # Case 1: The entire array's XOR is already non-zero
        if total_xor != 0:
            return len(nums)
            
        # Case 2: Total XOR is 0, we drop exactly one non-zero element
        return len(nums) - 1