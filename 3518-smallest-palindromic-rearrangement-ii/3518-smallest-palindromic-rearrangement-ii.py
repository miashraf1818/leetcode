from collections import Counter
import math

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        count = Counter(s)
        half_chars = []
        middle = ""
        for ch in sorted(count.keys()):
            half_chars.extend([ch] * (count[ch] // 2))
            if count[ch] % 2 == 1:
                middle = ch
        
        half_len = len(half_chars)
        freq = Counter(half_chars)
        unique_chars = sorted(freq.keys())
        LOG_K = math.log(k + 0.5)
        
        def cnf_compute(n, f):
            # Use min(f, n-f) for efficiency — C(n,f) = C(n, n-f)
            f = min(f, n - f)
            result = 1
            for i in range(f):
                result = result * (n - i) // (i + 1)
                # Cap early if ascending and already > k
                if result > k and i * 2 < n - 1:
                    return k + 1
            return result
        
        def count_perms_capped(freq, total):
            if total == 0:
                return 1
            # Fast log check
            log_result = math.lgamma(total + 1)
            for c in unique_chars:
                f = freq.get(c, 0)
                if f > 0:
                    log_result -= math.lgamma(f + 1)
            if log_result > LOG_K + 1:
                return k + 1
            # Exact computation
            result = 1
            remaining_n = total
            for c in unique_chars:
                f = freq.get(c, 0)
                if f == 0:
                    continue
                cnf = cnf_compute(remaining_n, f)
                result = min(result * cnf, k + 1)
                if result > k:
                    return k + 1
                remaining_n -= f
            return result
        
        total = count_perms_capped(freq, half_len)
        if total < k:
            return ""
        
        left_half = []
        remaining = half_len
        for i in range(half_len):
            for ch in unique_chars:
                if freq[ch] == 0:
                    continue
                freq[ch] -= 1
                remaining -= 1
                perms = count_perms_capped(freq, remaining)
                if perms >= k:
                    left_half.append(ch)
                    break
                else:
                    k -= perms
                    freq[ch] += 1
                    remaining += 1
        
        left = ''.join(left_half)
        return left + middle + left[::-1]