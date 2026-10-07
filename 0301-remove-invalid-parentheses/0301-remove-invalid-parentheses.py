from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        level = {s}
        while True:
            valid = list(filter(is_valid, level))
            if valid:
                return valid
            next_level = set()
            for string in level:
                for i, char in enumerate(string):
                    if char in '()':
                        next_level.add(string[:i] + string[i+1:])
            level = next_level