class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        stack = []
        pair = {}
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i
                
        res = []
        curr = 0
        direction = 1
        
        while curr < n:
            if s[curr] in '()':
                curr = pair[curr]
                direction = -direction
            else:
                res.append(s[curr])
            curr += direction
            
        return "".join(res)