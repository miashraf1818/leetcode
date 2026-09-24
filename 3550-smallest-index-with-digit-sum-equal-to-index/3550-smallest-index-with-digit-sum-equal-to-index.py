from typing import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if sum(int(d) for d in str(num)) == i:
                return i
        return -1