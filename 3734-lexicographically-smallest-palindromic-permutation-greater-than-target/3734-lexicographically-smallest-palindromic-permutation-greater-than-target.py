from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:

        n = len(s)
        counts = Counter(s)
        
        # 1. Validate if a palindrome can even be formed
        odd_chars = [ch for ch, cnt in counts.items() if cnt % 2 != 0]
        if len(odd_chars) > 1:
            return ""
            
        mid = odd_chars[0] if odd_chars else ""
        n_half = n // 2
        
        # Available characters we can freely distribute in the first half
        available = {ch: cnt // 2 for ch, cnt in counts.items()}
        
        # 2. Check if we can perfectly match the target's first half
        target_half = target[:n_half]
        can_form_exact = True
        for ch in set(target_half):
            if target_half.count(ch) > available.get(ch, 0):
                can_form_exact = False
                break
                
        if can_form_exact:
            P = target_half + mid + target_half[::-1]
            if P > target:
                return P
                
        # 3. Check for divergence in the first half, from right to left
        for p in range(n_half - 1, -1, -1):
            req = Counter(target[:p])
            
            # Can we form the target exactly up to index p?
            is_valid_prefix = True
            for ch, cnt in req.items():
                if available.get(ch, 0) < cnt:
                    is_valid_prefix = False
                    break
            
            if not is_valid_prefix:
                continue
                
            # Deduct the used characters from our available pool
            avail_after = {ch: cnt - req.get(ch, 0) for ch, cnt in available.items()}
            
            # Find the smallest available character strictly greater than target[p]
            best_c = None
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c > target[p] and avail_after.get(c, 0) > 0:
                    best_c = c
                    break
                    
            if best_c:
                # We found a valid divergence!
                avail_after[best_c] -= 1
                
                # The rest of the first half must be sorted ascending to be minimal
                rest = []
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if avail_after.get(c, 0) > 0:
                        rest.append(c * avail_after[c])
                        
                first_half = target[:p] + best_c + "".join(rest)
                P = first_half + mid + first_half[::-1]
                return P
                
        # 4. If no valid palindrome can be constructed
        return ""