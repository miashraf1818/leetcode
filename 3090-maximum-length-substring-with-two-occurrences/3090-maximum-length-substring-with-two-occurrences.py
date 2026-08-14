from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # Expand the window by including the current character
            freq[s[right]] += 1
            
            # If the character's frequency exceeds 2, shrink the window from the left
            while freq[s[right]] > 2:
                freq[s[left]] -= 1
                left += 1
                
            # Update the maximum valid substring length found so far
            max_len = max(max_len, right - left + 1)
            
        return max_len