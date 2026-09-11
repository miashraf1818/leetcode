class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        from typing import List

        counts = [0] * 10
        for d in digits:
            counts[d] += 1
            
        valid_count = 0
        
        # Step 2: Iterate through all possible 3-digit even numbers
        for num in range(100, 1000, 2):
            # Extract digits mathematically (faster than string conversion)
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            
            # Temporarily "use" the digits
            counts[d1] -= 1
            counts[d2] -= 1
            counts[d3] -= 1
            
            # If we didn't drop below 0 for any digit, we can form this number
            if counts[d1] >= 0 and counts[d2] >= 0 and counts[d3] >= 0:
                valid_count += 1
                
            # Backtrack and "return" the digits for the next iteration
            counts[d1] += 1
            counts[d2] += 1
            counts[d3] += 1
            
        return valid_count