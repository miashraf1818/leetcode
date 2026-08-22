class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp = n
        d_sum = 0
        d_prod = 1
        
        # Extract digits one by one
        while temp > 0:
            digit = temp % 10
            d_sum += digit
            d_prod *= digit
            temp //= 10
            
        # Check divisibility condition
        return n % (d_sum + d_prod) == 0