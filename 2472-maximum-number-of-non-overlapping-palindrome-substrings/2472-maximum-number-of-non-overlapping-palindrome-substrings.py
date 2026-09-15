class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        intervals = []
        
        # Step 1 & 2: Center Expansion to find the smallest valid palindromes
        # There are 2n - 1 possible centers (n single characters, n-1 pairs)
        for i in range(2 * n - 1):
            left = i // 2
            right = left + i % 2
            
            # Expand outwards while characters match and stay within bounds
            while left >= 0 and right < n and s[left] == s[right]:
                # If we meet the minimum length requirement
                if right - left + 1 >= k:
                    intervals.append((left, right))
                    # Stop expanding for this center! 
                    # Any larger palindrome here will strictly contain this one,
                    # making it a worse candidate for maximizing non-overlapping selections.
                    break
                left -= 1
                right += 1
                
        # Step 3: Greedy Interval Scheduling
        # Sort intervals by their end index to greedily pack as many as possible
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        last_end = -1
        
        for left, right in intervals:
            # If the current palindrome starts strictly after the last selected one ends
            if left > last_end:
                count += 1
                last_end = right
                
        return count       