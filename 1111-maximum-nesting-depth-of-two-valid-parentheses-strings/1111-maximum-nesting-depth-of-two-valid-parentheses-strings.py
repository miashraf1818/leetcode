from typing import List

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans = []
        d = 0  # Tracks current nesting depth
        
        for char in seq:
            if char == '(':
                # Assign based on current depth, then increment depth
                ans.append(d % 2)
                d += 1
            else:
                # Decrement depth first, then assign based on parent depth
                d -= 1
                ans.append(d % 2)
                
        return ans