class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        from typing import List
        result = [0] * k
        
        # counts[r] tracks the number of subarrays ending at the PREVIOUS index 
        # with a product modulo k equal to r.
        counts = [0] * k
        
        for num in nums:
            new_counts = [0] * k
            
            # To prevent large number multiplications, take modulo immediately
            val = num % k
            
            # 1. Start a new subarray with just the current element
            new_counts[val] += 1
            
            # 2. Extend all existing subarrays ending at the previous index
            for r in range(k):
                if counts[r] > 0:
                    new_r = (r * val) % k
                    new_counts[new_r] += counts[r]
                    
            # 3. Accumulate to the global result and update counts for the next iteration
            for r in range(k):
                result[r] += new_counts[r]
                counts[r] = new_counts[r]
                
        return result