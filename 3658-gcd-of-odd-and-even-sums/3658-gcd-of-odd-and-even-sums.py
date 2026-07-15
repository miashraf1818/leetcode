from math import gcd
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_odd  = n * n          # sum of first n odd numbers  = n²
        sum_even = n * (n + 1)    # sum of first n even numbers = n(n+1)
        return gcd(sum_odd, sum_even)