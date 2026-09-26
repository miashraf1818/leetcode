from typing import List

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = {k: v for k, v in knowledge}
        res = []
        key = []
        in_bracket = False
        
        for char in s:
            if char == '(':
                in_bracket = True
            elif char == ')':
                in_bracket = False
                res.append(d.get("".join(key), '?'))
                key = []
            elif in_bracket:
                key.append(char)
            else:
                res.append(char)
                
        return "".join(res)