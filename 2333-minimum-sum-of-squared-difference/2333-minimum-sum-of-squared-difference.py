class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        from typing import List

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
        total_k = k1 + k2
        
        if sum(diffs) <= total_k:
            return 0
            
        max_d = max(diffs)
        count = [0] * (max_d + 1)
        for d in diffs:
            count[d] += 1
            
        for i in range(max_d, 0, -1):
            if count[i] > 0:
                take = min(total_k, count[i])
                count[i] -= take
                count[i - 1] += take
                total_k -= take
                if total_k == 0:
                    break
                    
        return sum(i * i * count[i] for i in range(max_d + 1))