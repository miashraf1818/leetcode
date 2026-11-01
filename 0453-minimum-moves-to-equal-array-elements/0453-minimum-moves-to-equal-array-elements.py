from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_val = min(nums)
        return sum(x - min_val for x in nums)