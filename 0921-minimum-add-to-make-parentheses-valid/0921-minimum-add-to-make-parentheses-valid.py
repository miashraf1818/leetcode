class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_cnt = 0
        moves = 0
        
        for char in s:
            if char == '(':
                open_cnt += 1
            else:
                if open_cnt > 0:
                    open_cnt -= 1
                else:
                    moves += 1
                    
        return moves + open_cnt