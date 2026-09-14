
from typing import List

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # Extract coordinates for readability
        x1_1, y1_1, x2_1, y2_1 = rec1
        x1_2, y1_2, x2_2, y2_2 = rec2
        
        # Check if the 1D projections on the x-axis and y-axis both overlap
        x_overlap = min(x2_1, x2_2) > max(x1_1, x1_2)
        y_overlap = min(y2_1, y2_2) > max(y1_1, y1_2)
        
        return x_overlap and y_overlap