class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        needed_right = 0
        
        for char in s:
            if char == '(':
                needed_right += 2
                if needed_right % 2 != 0:
                    res += 1
                    needed_right -= 1
            else:
                needed_right -= 1
                if needed_right < 0:
                    res += 1
                    needed_right += 2
                    
        return res + needed_right
        