import math

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        
        # 1. Gather all unique divisors of n
        divisors = []
        for i in range(1, int(math.isqrt(n)) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
        
        total_sum = 0
        
        # 2. Check each candidate divisor k
        for k in divisors:
            is_valid = True
            prev_max = float('-inf')
            
            # Process the array block by block
            for start in range(0, n, k):
                block = nums[start:start + k]
                
                # Step A: Count "drops" in a circular fashion within the block
                drops = 0
                drop_index = -1
                for i in range(k):
                    if block[i] > block[(i + 1) % k]:
                        drops += 1
                        drop_index = i
                
                # If there's more than 1 drop, it can never be cyclically sorted
                if drops > 1:
                    is_valid = False
                    break
                
                # Step B: Determine the minimum and maximum if we were to rotate it properly
                if drops == 0:
                    # Already sorted internally
                    curr_min = block[0]
                    curr_max = block[-1]
                else:
                    # If there's exactly 1 drop, the array must be unrolled at the drop point.
                    # The element right after the drop becomes the start of the sorted sequence.
                    curr_min = block[(drop_index + 1) % k]
                    curr_max = block[drop_index]
                
                # Step C: Verify global sorted order between consecutive blocks
                if curr_min < prev_max:
                    is_valid = False
                    break
                
                prev_max = curr_max
            
            if is_valid:
                total_sum += k
                
        return total_sum
