from typing import List
import collections

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        # Count the frequencies of stones modulo 3
        counts = collections.Counter(x % 3 for x in stones)
        c0, c1, c2 = counts[0], counts[1], counts[2]
        
        # If the number of 0 mod 3 stones is even
        if c0 % 2 == 0:
            # Alice wins as long as she has both 1s and 2s to form a sequence
            return c1 > 0 and c2 > 0
        else:
            # If the number of 0 mod 3 stones is odd, the parity flips.
            # Alice needs a significant imbalance to outlast Bob.
            return abs(c1 - c2) > 2