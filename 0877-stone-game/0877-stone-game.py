from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Alice can always force a win by taking either all even-indexed 
        # or all odd-indexed piles.
        return True