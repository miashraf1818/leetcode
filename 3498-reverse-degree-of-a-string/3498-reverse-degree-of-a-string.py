class Solution:
    def reverseDegree(self, s: str) -> int:
        total_degree = 0
        
        # enumerate(s, 1) directly provides the 1-based index for each character
        for i, char in enumerate(s, 1):
            # Mathematically map 'a' (97) to 26, 'b' (98) to 25, ..., 'z' (122) to 1
            reversed_val = 123 - ord(char)
            
            # Accumulate the product of the reversed value and the 1-based index
            total_degree += reversed_val * i
            
        return total_degree