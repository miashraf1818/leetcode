class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        from math import gcd
        
        # Check if `t` is achievable with digits 1-9 (only divisible by prime factors 2, 3, 5, 7)
        temp = t
        for p in [2, 3, 5, 7]:
            while temp % p == 0:
                temp //= p
        if temp > 1:
            return "-1"
            
        n = len(num)
        digits = [int(c) for c in num]
        
        # DP memoization to compute the absolute minimum digits needed to pack leftover factors of 2 and 3
        memo_23 = {}
        def min_digits_23(a, b):
            a, b = max(0, a), max(0, b)
            if a == 0 and b == 0:
                return 0
            if (a, b) in memo_23:
                return memo_23[(a, b)]
            
            ans = float('inf')
            # Pack using digit '8' (absorbs up to three 2s)
            if a > 0:
                ans = min(ans, 1 + min_digits_23(a - 3, b))
            # Pack using digit '9' (absorbs up to two 3s)
            if b > 0:
                ans = min(ans, 1 + min_digits_23(a, b - 2))
            # Pack using digit '6' (absorbs one 2, one 3)
            if a > 0 or b > 0:
                ans = min(ans, 1 + min_digits_23(a - 1, b - 1))
                
            memo_23[(a, b)] = ans
            return ans
            
        def min_digits_needed(rem):
            """Total absolute minimum count of digits required to meet the factors of `rem`."""
            if rem == 1: return 0
            cnt2 = cnt3 = cnt5 = cnt7 = 0
            while rem % 2 == 0: cnt2 += 1; rem //= 2
            while rem % 3 == 0: cnt3 += 1; rem //= 3
            while rem % 5 == 0: cnt5 += 1; rem //= 5
            while rem % 7 == 0: cnt7 += 1; rem //= 7
            
            # Digits `5` and `7` strictly consume one character slot each. Combine with 2's & 3's min packing counts.
            return cnt5 + cnt7 + min_digits_23(cnt2, cnt3)
            
        def smallest_suffix(rem, length):
            """Greedily construct the lexicographically smallest sequence of digits matching exactly `length`."""
            if length == 0:
                return [] if rem == 1 else None
            
            result = []
            for pos in range(length):
                placed = False
                for d in range(1, 10):
                    new_rem = rem // gcd(rem, d)
                    if min_digits_needed(new_rem) <= length - pos - 1:
                        result.append(d)
                        rem = new_rem
                        placed = True
                        break
                if not placed:
                    return None
            return result
            
        # Precompute sequential cumulative prefix tracking bounded entirely by `t` (O(N) memory scale-down factor)
        pref_gcd = [1] * (n + 1)
        for i in range(n):
            pref_gcd[i+1] = gcd(t, pref_gcd[i] * digits[i])
            
        # Case 0: Check if the unmutated base state is cleanly valid
        if "0" not in num and pref_gcd[n] == t:
            return num
            
        zero_idx = num.find("0")
        
        # Case 1: Attempt preserving a prefix right-to-left and inflating exactly 1 digit
        for i in range(n - 1, -1, -1):
            if zero_idx != -1 and zero_idx < i:
                continue
                
            p_gcd = pref_gcd[i]
            
            for d in range(digits[i] + 1, 10):
                new_gcd = gcd(t, p_gcd * d)
                rem = t // new_gcd
                suffix_len = n - i - 1
                
                if min_digits_needed(rem) <= suffix_len:
                    suffix = smallest_suffix(rem, suffix_len)
                    if suffix is not None:
                        ans = digits[:i] + [d] + suffix
                        return "".join(map(str, ans))
                        
        # Case 2: Out of slots/viable numbers above prefix length bounds. Build via a globally lengthened threshold 
        length = max(n + 1, min_digits_needed(t))
        suffix = smallest_suffix(t, length)
        
        return "".join(map(str, suffix))