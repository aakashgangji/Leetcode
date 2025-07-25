"""
Reverse bits of a given 32 bits unsigned integer.
Input: n = 43261596
Output: 964176192
Explanation:
Integer	    Binary
43261596	00000010100101000001111010011100
964176192	00111001011110000010100101000000

"""

def reverseBits(self, n: int) -> int:
    res=0
    for i in range(32):
        bit=(n>>i)&1
        res=res|(bit<<(31-i))
    return res

n = 43261596
print(reverseBits(None,n))
