class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        max_i=60
        for k in range(1, max_i+1):
            rem = num1 - k * num2
            if rem<k:
                continue
            if bin(rem).count('1') <= k:
                return k
        return -1
sol=Solution()
print(sol.makeTheIntegerZero(3,-2))