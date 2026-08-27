class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        from collections import Counter
        
        n = len(s)
        counts = Counter(s)
        
        # Step 1: Find the maximum prefix of target that can be formed
        p = 0
        while p < n and counts[target[p]] > 0:
            counts[target[p]] -= 1
            p += 1
            
        # Step 2: Iterate backwards to find the optimal divergence point
        for i in range(min(p, n - 1), -1, -1):
            # If target[i] was matched in the prefix, return it to the available pool
            if i < p:
                counts[target[i]] += 1
                
            # Look for the smallest available character strictly greater than target[i]
            best_c = None
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c > target[i] and counts[c] > 0:
                    best_c = c
                    break
                    
            if best_c:
                # We found a valid point of divergence
                counts[best_c] -= 1
                
                # Step 3: Build the resulting string
                # 1. The matched prefix
                # 2. The strictly greater character
                res = [target[:i], best_c]
                
                # 3. The remaining characters in ascending order
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if counts[c] > 0:
                        res.append(c * counts[c])
                        
                return "".join(res)
                
        # Step 4: If no valid permutation can be formed
        return ""