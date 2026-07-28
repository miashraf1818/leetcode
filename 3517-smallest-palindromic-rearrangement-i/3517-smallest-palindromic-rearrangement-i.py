class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter
        
        count = Counter(s)
        
        # Build the left half using sorted characters
        half = []
        middle = ""
        
        for ch in sorted(count.keys()):
            half.extend([ch] * (count[ch] // 2))
            if count[ch] % 2 == 1:
                middle = ch  # at most one odd character (guaranteed palindrome)
        
        left = ''.join(half)
        return left + middle + left[::-1]