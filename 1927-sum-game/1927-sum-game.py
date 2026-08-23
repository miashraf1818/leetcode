class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        sum_l = sum_r = 0
        q_l = q_r = 0
        
        # Parse the left half
        for i in range(half):
            if num[i] == '?':
                q_l += 1
            else:
                sum_l += int(num[i])
                
        # Parse the right half
        for i in range(half, n):
            if num[i] == '?':
                q_r += 1
            else:
                sum_r += int(num[i])
                
        # If total '?' is odd, Alice gets the last move and trivially wins
        if (q_l + q_r) % 2 != 0:
            return True
            
        # If total '?' is even, Bob wins if the initial sum difference perfectly 
        # offsets the expected gain from the excess '?' pairs.
        if (sum_l - sum_r) == -9 * (q_l - q_r) // 2:
            return False
            
        return True


        