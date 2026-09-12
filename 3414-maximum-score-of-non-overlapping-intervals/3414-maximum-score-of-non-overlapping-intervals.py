from typing import List
from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
        # Pair each interval with its original index and sort by start time
        arr = sorted((intervals[i][0], intervals[i][1], intervals[i][2], i) for i in range(n))
        starts = [x[0] for x in arr]
        
        # dp[i][k] stores: (-weight, tuple_of_original_indices)
        # Using negative weight lets us use min() to get max weight and lexicographically smallest indices simultaneously.
        dp = [[(0, ())] * 5 for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            _, r, w, orig_idx = arr[i]
            
            # Find the first interval j that strictly starts after interval i ends
            j = bisect_right(starts, r)
            
            for k in range(1, 5):
                # Option 1: Skip this interval
                skip_val = dp[i + 1][k]
                
                # Option 2: Take this interval
                prev_w, prev_indices = dp[j][k - 1]
                take_w = prev_w - w  # Subtraction because weights are stored as negative
                
                # Keep the resulting indices sorted to maintain strict lexicographical order properties
                take_indices = tuple(sorted(prev_indices + (orig_idx,)))
                take_val = (take_w, take_indices)
                
                # min() seamlessly handles picking the best weight, tying breaking with the smallest indices
                dp[i][k] = skip_val if skip_val < take_val else take_val
                
        # Return the indices of the optimal configuration for picking up to 4 intervals
        return list(dp[0][4][1])