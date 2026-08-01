class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        from functools import lru_cache
        n = len(nums)
        
        @lru_cache(maxsize=None)
        def dp(left, right):
            # Returns max score difference (current player - other player)
            # for nums[left..right]
            if left == right:
                return nums[left]
            take_left  = nums[left]  - dp(left + 1, right)
            take_right = nums[right] - dp(left, right - 1)
            return max(take_left, take_right)
        
        return dp(0, n - 1) >= 0