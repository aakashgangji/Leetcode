# You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.
# Return the number of distinct ways to climb to the top of the staircase.
# Example 1:
# Input: n = 2
# Output: 2
# Explanation:
# 1 + 1 = 2
# 2 = 2
# Example 2:
# Input: n = 3
# Output: 3

def climbStairs(self, n: int) -> int:
    one,two=1,1

    for i in range(n-1):
        temp=one
        one=one+two
        two=temp
    return one

n=5
print(climbStairs(None,n))