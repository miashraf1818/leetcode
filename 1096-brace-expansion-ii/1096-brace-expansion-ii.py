from typing import List

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stack = [expression]
        seen = {expression}
        res = set()
        
        while stack:
            expr = stack.pop()
            
            if '{' not in expr:
                res.add(expr)
                continue
                
            # Find the first closing brace and its corresponding innermost opening brace
            r = expr.find('}')
            l = expr.rfind('{', 0, r)
            
            # The parts before and after the innermost braces
            before = expr[:l]
            after = expr[r+1:]
            
            # The choices inside the innermost braces
            choices = expr[l+1:r].split(',')
            
            for choice in choices:
                new_expr = before + choice + after
                if new_expr not in seen:
                    seen.add(new_expr)
                    stack.append(new_expr)
                    
        return sorted(list(res))