from typing import List


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        base1, mod1 = 1000003, 10**9 + 7
        base2, mod2 = 1000033, 10**9 + 9

        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow1[i] = (pow1[i - 1] * base1) % mod1
            pow2[i] = (pow2[i - 1] * base2) % mod2

        def has_unique(length: int) -> bool:
            if length == n:
                return True
            h1 = h2 = 0
            for i in range(length):
                val = nums[i] + 1
                h1 = (h1 * base1 + val) % mod1
                h2 = (h2 * base2 + val) % mod2

            seen = {(h1, h2): 1}
            p1, p2 = pow1[length - 1], pow2[length - 1]

            for i in range(length, n):
                out_val = nums[i - length] + 1
                in_val = nums[i] + 1

                h1 = ((h1 - out_val * p1) * base1 + in_val) % mod1
                h2 = ((h2 - out_val * p2) * base2 + in_val) % mod2

                key = (h1, h2)
                seen[key] = seen.get(key, 0) + 1

            return any(cnt == 1 for cnt in seen.values())

        lo, hi = 1, n
        ans = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if has_unique(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans