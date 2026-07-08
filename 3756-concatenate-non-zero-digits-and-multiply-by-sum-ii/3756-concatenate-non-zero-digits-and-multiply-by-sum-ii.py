class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        m = len(s)
        
        # prefix_x[i] = x value formed by non-zero digits in s[0..i-1], mod MOD
        # prefix_sum[i] = sum of non-zero digits in s[0..i-1]
        # prefix_count[i] = count of non-zero digits in s[0..i-1]
        
        prefix_x = [0] * (m + 1)
        prefix_sum = [0] * (m + 1)
        prefix_count = [0] * (m + 1)
        
        for i in range(m):
            d = int(s[i])
            if d != 0:
                prefix_x[i+1] = (prefix_x[i] * 10 + d) % MOD
                prefix_sum[i+1] = prefix_sum[i] + d
                prefix_count[i+1] = prefix_count[i] + 1
            else:
                prefix_x[i+1] = prefix_x[i]
                prefix_sum[i+1] = prefix_sum[i]
                prefix_count[i+1] = prefix_count[i]
        
        # Precompute powers of 10 mod MOD
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = pow10[i-1] * 10 % MOD
        
        result = []
        for l, r in queries:
            # non-zero digits count in s[l..r]
            cnt = prefix_count[r+1] - prefix_count[l]
            
            # sum of non-zero digits in s[l..r]
            digit_sum = prefix_sum[r+1] - prefix_sum[l]
            
            if digit_sum == 0:
                result.append(0)
                continue
            
            # x for s[l..r]:
            # = (x of full s[0..r]) - (x of s[0..l-1]) * 10^cnt
            x = (prefix_x[r+1] - prefix_x[l] * pow10[cnt]) % MOD
            
            result.append(x * digit_sum % MOD)
        
        return result