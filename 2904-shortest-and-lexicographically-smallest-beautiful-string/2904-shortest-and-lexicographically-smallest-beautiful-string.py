class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # Step 1: Record all indices where '1' occurs
        ones = [i for i, char in enumerate(s) if char == '1']
        
        # Step 2: Check if there are even enough '1's to form a beautiful substring
        if len(ones) < k:
            return ""
            
        best_str = ""
        best_len = float('inf')
        
        # Step 3 & 4: Evaluate exactly the substrings bounded by k '1's
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]
            
            sub = s[start:end + 1]
            sub_len = len(sub)
            
            # Update if we find a strictly shorter one, 
            # or a same-length one that is lexicographically smaller
            if sub_len < best_len:
                best_len = sub_len
                best_str = sub
            elif sub_len == best_len:
                if sub < best_str:
                    best_str = sub
                    
        return best_str