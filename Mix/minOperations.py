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
    def minimumOperations(self, nums: List[int]) -> int:
        count = [0, 0, 0]
        
        for num in nums:
            count[num % 3] += 1
        
        operations = 0
        
        # Pair elements with remainder 1 and 2
        pair_count = min(count[1], count[2])
        operations += pair_count
        count[1] -= pair_count
        count[2] -= pair_count
        
        # Handle remaining elements with remainder 1
        if count[1] > 0:
            operations += (count[1] // 3) * 2
            if count[1] % 3 != 0:
                operations += 2
        
        # Handle remaining elements with remainder 2
        if count[2] > 0:
            operations += (count[2] // 3) * 2
            if count[2] % 3 != 0:
                operations += 2
        
        return operations