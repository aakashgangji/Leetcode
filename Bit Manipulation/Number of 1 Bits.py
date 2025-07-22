"""
You are given an unsigned integer n. Return the number of 1 bits in its binary representation.

You may assume n is a non-negative integer which fits within 32-bits.
"""
def hammingWeight(self, n: int) -> int:
    res=0
    while n:
        res+=n%2
        n=n>>1
    return res

n = 0b01111111111111111111111111111101
print(hammingWeight(None,n))