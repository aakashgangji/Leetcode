"""Sum of Two Integers
Given two integers a and b, return the sum of the two integers without using the + and - operators.
Example 1:
Input: a = 1, b = 1
Output: 2
Example 2:
Input: a = 4, b = 7
Output: 11
"""

def getSum(a,b):
    max_int=0x7FFFFFFFF
    mask=0xFFFFFFFF
    while b !=0:
        xor=(a^b)&mask
        carry=((a&b)<<1)&mask
        a,b=xor,carry
    return a if a<=max_int else ~(a^mask)
a=7
b=13
print(getSum(a,b))
print(getSum(4,3))