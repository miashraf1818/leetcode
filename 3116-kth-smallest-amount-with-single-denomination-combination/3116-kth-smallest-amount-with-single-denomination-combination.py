from typing import List
import math

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # Step 1: Optimize by filtering out redundant coins (multiples of other smaller coins)
        filtered_coins = []
        coins.sort()
        for c in coins:
            if not any(c % fc == 0 for fc in filtered_coins):
                filtered_coins.append(c)
        
        n = len(filtered_coins)
        
        # Step 2: Precalculate LCMs for all possible bitwise subsets to use in PIE
        pos_lcms = []
        neg_lcms = []
        
        # Iterate through all 2^n - 1 non-empty subsets
        for i in range(1, 1 << n):
            current_lcm = 1
            bits = 0
            for j in range(n):
                if (i >> j) & 1:
                    current_lcm = math.lcm(current_lcm, filtered_coins[j])
                    bits += 1
            
            # Odd number of elements -> Add to total
            if bits % 2 == 1:
                pos_lcms.append(current_lcm)
            # Even number of elements -> Subtract from total
            else:
                neg_lcms.append(current_lcm)
                
        # Step 3: Binary Search for the k-th smallest amount
        low = 1
        high = filtered_coins[0] * k
        
        while low < high:
            mid = (low + high) // 2
            
            # Principle of Inclusion-Exclusion evaluation
            c = 0
            for val in pos_lcms:
                c += mid // val
            for val in neg_lcms:
                c -= mid // val
                
            # If we've formed at least k amounts, the answer might be mid or smaller
            if c >= k:
                high = mid
            else:
                low = mid + 1
                
        return low