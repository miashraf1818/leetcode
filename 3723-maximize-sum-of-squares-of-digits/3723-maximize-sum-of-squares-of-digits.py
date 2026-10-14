class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum < 1 or sum > 9 * num:
            return ""
        
        res = []
        rem_sum = sum
        
        for i in range(num):
            low = 1 if i == 0 and num > 1 else 0
            high = min(9, rem_sum)
            
            for d in range(high, low - 1, -1):
                if 0 <= rem_sum - d <= 9 * (num - 1 - i):
                    res.append(str(d))
                    rem_sum -= d
                    break
                    
        return "".join(res)