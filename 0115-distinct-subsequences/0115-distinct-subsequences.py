class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # If the target is longer than the source, it's impossible to form
        if n > m:
            return 0
            
        # dp[j] stores the number of distinct subsequences forming t[:j]
        dp = [0] * (n + 1)
        
        # Base case: 1 way to form an empty string target
        dp[0] = 1
        
        # Iterate through each character of the source string s
        for i in range(1, m + 1):
            # Iterate backwards through t to avoid overwriting dependencies for the current step
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    # If characters match, add combinations of the prefix without this character
                    dp[j] += dp[j - 1]
                    
        return dp[n]