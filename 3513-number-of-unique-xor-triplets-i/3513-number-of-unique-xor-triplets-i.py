class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return 1  # only triplet: nums[0]^nums[0]^nums[0] = nums[0]
        
        if n == 2:
            return 2  # {nums[0], nums[1]}
        
        # For n >= 3:
        # nums is a permutation of [1..n]
        # With all values 1..n available, XOR of any 3 can produce 0..2^bits-1
        # where bits = number of bits needed to represent n
        # Answer = 2^bits where bits = floor(log2(n)) + 1
        
        bits = n.bit_length()
        return 1 << bits