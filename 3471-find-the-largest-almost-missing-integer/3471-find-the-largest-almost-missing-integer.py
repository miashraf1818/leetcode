from typing import List
from collections import defaultdict

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        n = len(nums)
        
        # Iterate over all possible starting indices for a subarray of size k
        for i in range(n - k + 1):
            # Use a set to ensure each number is counted only once per subarray
            unique_in_window = set(nums[i:i + k])
            for num in unique_in_window:
                counts[num] += 1
                
        # Find the maximum integer that appears in exactly one subarray
        max_almost_missing = -1
        for num, count in counts.items():
            if count == 1:
                max_almost_missing = max(max_almost_missing, num)
                
        return max_almost_missing