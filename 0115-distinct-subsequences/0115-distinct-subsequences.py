class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # If the target string is longer, it's impossible to form it as a subsequence
        if n > m:
            return 0
            
        # dp[j] stores the number of distinct subsequences forming t of length j
        dp = [0] * (n + 1)
        
        # Base case: 1 way to form an empty prefix of t
        dp[0] = 1
        
        # Iterate through each character of the source string s
        for i in range(m):
            # Iterate backwards through t to avoid overwriting dependencies
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    # If characters match, add combinations of the prefix without this character
                    dp[j + 1] += dp[j]
                    
        return dp[n]