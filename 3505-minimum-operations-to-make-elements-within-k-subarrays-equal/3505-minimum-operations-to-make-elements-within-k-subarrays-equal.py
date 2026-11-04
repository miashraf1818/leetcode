from typing import List
import heapq

class Solution:
    def minimumOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        costs = [0] * (n - x + 1)
        
        lo = [] 
        hi = [] 
        lo_delayed = {}
        hi_delayed = {}
        lo_size = 0
        hi_size = 0
        lo_sum = 0
        hi_sum = 0

        def prune_lo():
            while lo and -lo[0] in lo_delayed:
                val = -lo[0]
                lo_delayed[val] -= 1
                if lo_delayed[val] == 0:
                    del lo_delayed[val]
                heapq.heappop(lo)

        def prune_hi():
            while hi and hi[0] in hi_delayed:
                val = hi[0]
                hi_delayed[val] -= 1
                if hi_delayed[val] == 0:
                    del hi_delayed[val]
                heapq.heappop(hi)

        def balance():
            nonlocal lo_size, hi_size, lo_sum, hi_sum
            prune_lo()
            prune_hi()
            while lo_size > hi_size + 1:
                val = -heapq.heappop(lo)
                lo_size -= 1
                lo_sum -= val
                heapq.heappush(hi, val)
                hi_size += 1
                hi_sum += val
                prune_lo()
            while hi_size > lo_size:
                val = heapq.heappop(hi)
                hi_size -= 1
                hi_sum -= val
                heapq.heappush(lo, -val)
                lo_size += 1
                lo_sum += val
                prune_hi()

        def insert(val):
            nonlocal lo_size, hi_size, lo_sum, hi_sum
            prune_lo()
            if not lo or val <= -lo[0]:
                heapq.heappush(lo, -val)
                lo_size += 1
                lo_sum += val
            else:
                heapq.heappush(hi, val)
                hi_size += 1
                hi_sum += val
            balance()

        def erase(val):
            nonlocal lo_size, hi_size, lo_sum, hi_sum
            prune_lo()
            prune_hi()
            if lo and val <= -lo[0]:
                lo_delayed[val] = lo_delayed.get(val, 0) + 1
                lo_size -= 1
                lo_sum -= val
                if val == -lo[0]:
                    prune_lo()
            else:
                hi_delayed[val] = hi_delayed.get(val, 0) + 1 if val not in hi_delayed else hi_delayed[val] + 1
                hi_size -= 1
                hi_sum -= val
                if hi and val == hi[0]:
                    prune_hi()
            balance()

        for i in range(x):
            insert(nums[i])
        
        prune_lo()
        prune_hi()
        median = -lo[0]
        cost = median * lo_size - lo_sum + hi_sum - median * hi_size
        costs[0] = cost

        for i in range(1, n - x + 1):
            erase(nums[i - 1])
            insert(nums[i + x - 1])
            prune_lo()
            prune_hi()
            median = -lo[0]
            cost = median * lo_size - lo_sum + hi_sum - median * hi_size
            costs[i] = cost

        m_c = len(costs)
        dp = [float('inf')] * m_c
        curr_min = float('inf')
        for i in range(m_c):
            curr_min = min(curr_min, costs[i])
            dp[i] = curr_min

        for j in range(2, k + 1):
            next_dp = [float('inf')] * m_c
            run_min = float('inf')
            for i in range(m_c):
                p = i - x
                if p >= 0:
                    run_min = min(run_min, dp[p])
                if run_min != float('inf'):
                    next_dp[i] = run_min + costs[i]
                if i > 0:
                    next_dp[i] = min(next_dp[i], next_dp[i - 1])
            dp = next_dp

        return dp[-1]

    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        return self.minimumOperations(nums, x, k)