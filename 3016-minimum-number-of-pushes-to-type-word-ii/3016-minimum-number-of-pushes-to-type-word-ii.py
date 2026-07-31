from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = sorted(Counter(word).values(), reverse=True)
        result = 0
        for i, count in enumerate(freq):
            result += count * ((i // 8) + 1)
        return result