class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        def get_cost(k):
            return k * costBoth + max(0, need1 - k) * cost1 + max(0, need2 - k) * cost2
            
        return min(get_cost(0), get_cost(need1), get_cost(need2))

    def minCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        return self.minimumCost(cost1, cost2, costBoth, need1, need2)