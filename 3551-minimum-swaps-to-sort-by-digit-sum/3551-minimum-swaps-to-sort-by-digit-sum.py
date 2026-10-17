from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(x: int) -> int:
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s

        n = len(nums)
        target = sorted(nums, key=lambda x: (digit_sum(x), x))
        val_to_target_pos = {val: i for i, val in enumerate(target)}
        
        pos = [val_to_target_pos[num] for num in nums]
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            if not visited[i] and pos[i] != i:
                cycle_size = 0
                curr = i
                while not visited[curr]:
                    visited[curr] = True
                    curr = pos[curr]
                    cycle_size += 1
                swaps += cycle_size - 1
                
        return swaps