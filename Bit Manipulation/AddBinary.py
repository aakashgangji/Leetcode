"""Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=""
        carry=0
        i,j=len(a)-1,len(b)-1
        while i>=0 or j>=0 or carry:
            sum=carry
            if i>=0:
                sum+=int(a[i])
                i-=1
            if j>=0:
                sum+=int(b[j])
                j-=1
            res=str(sum%2)+res
            carry=sum//2
        return res