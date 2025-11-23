"""
You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.

Return the minimum number of operations to make all elements of nums divisible by 3.

 

Example 1:

Input: nums = [1,2,3,4]

Output: 3

Explanation:

All array elements can be made divisible by 3 using 3 operations:

Subtract 1 from 1.
Add 1 to 2.
Subtract 1 from 4.
Example 2:

Input: nums = [3,6,9]

Output: 0
"""
class Solution:
  def minimumOperations(self, nums: list[int]) -> int:
    return sum(num % 3 != 0 for num in nums)
  
# Example usage:
solution = Solution()
print(solution.minimumOperations([1, 2, 3, 4]))  # Output: 3
print(solution.minimumOperations([3, 6, 9]))     # Output: 0