

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        
        # best_till[i] stores the minimum length of a valid sub-array ending at or before index i
        best_till = [float('inf')] * n
        
        left = 0
        current_sum = 0
        min_len = float('inf')
        ans = float('inf')
        
        for right in range(n):
            current_sum += arr[right]
            
            # Shrink the window if the sum exceeds the target
            while current_sum > target:
                current_sum -= arr[left]
                left += 1
                
            # If we find a valid sub-array
            if current_sum == target:
                curr_len = right - left + 1
                
                # Check if there's a valid non-overlapping sub-array to the left
                if left > 0 and best_till[left - 1] != float('inf'):
                    ans = min(ans, curr_len + best_till[left - 1])
                    
                # Update the shortest sub-array seen so far
                min_len = min(min_len, curr_len)
                
            # Record the best minimum length up to the current right index
            best_till[right] = min_len
            
        return ans if ans != float('inf') else -1