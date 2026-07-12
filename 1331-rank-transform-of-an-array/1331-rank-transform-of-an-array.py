class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank_map = {val: i + 1 for i, val in enumerate(sorted(set(arr)))}
        return [rank_map[val] for val in arr]