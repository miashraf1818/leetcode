from typing import List
from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        masks = defaultdict(int)
        
        # Populate bitmasks for rows that have reservations
        for r, c in reservedSeats:
            if 2 <= c <= 5:
                masks[r] |= 1  # Left block obstructed
            if 4 <= c <= 7:
                masks[r] |= 2  # Middle block obstructed
            if 6 <= c <= 9:
                masks[r] |= 4  # Right block obstructed
                
        # Unaffected rows can cleanly accommodate 2 families each
        ans = (n - len(masks)) * 2
        
        # Determine capacity for the affected rows
        for mask in masks.values():
            if mask & 5 == 0:
                # Left and Right are both free (Middle might theoretically be free too, but doesn't allow a 3rd)
                ans += 2
            elif (mask & 1) == 0 or (mask & 4) == 0 or (mask & 2) == 0:
                # At least one valid distinct block is free
                ans += 1
                
        return ans