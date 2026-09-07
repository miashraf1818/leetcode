class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        
        # last_count[i] stores the number of distinct subsequences ending with the i-th letter
        last_count = [0] * 26
        
        # Total number of distinct non-empty subsequences formed so far
        total = 0
        
        for char in s:
            char_idx = ord(char) - ord('a')
            
            # The number of new subsequences we can form ending with the current character.
            # This is equal to all previous subsequences (total) + the single character itself (+ 1).
            new_add = (total + 1) % MOD
            
            # We add the new subsequences and subtract the ones we have already counted 
            # (which is the previous value stored in last_count for this character)
            total = (total + new_add - last_count[char_idx]) % MOD
            
            # Update the count of subsequences ending with this character
            last_count[char_idx] = new_add
            
        return total