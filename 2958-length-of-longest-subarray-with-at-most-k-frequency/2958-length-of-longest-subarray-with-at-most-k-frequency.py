from typing import List
from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        max_len = 0
        
        for right in range(len(nums)):
            # Add the current element to the window's frequency map
            freq[nums[right]] += 1
            
            # If the current element exceeds the allowed frequency k, 
            # shrink the window from the left until it is valid again.
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1
                
            # Update the maximum length of a valid subarray found so far
            max_len = max(max_len, right - left + 1)
            
        return max_len