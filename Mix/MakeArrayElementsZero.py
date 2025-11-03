"""
You are given an integer array nums.
Start by selecting a starting position curr such that nums[curr] == 0, and choose a movement direction of either left or right.
After that, you repeat the following process:
If curr is out of the range [0, n - 1], this process ends.
If nums[curr] == 0, move in the current direction by incrementing curr if you are moving right, or decrementing curr if you are moving left.
Else if nums[curr] > 0:
Decrement nums[curr] by 1.
Reverse your movement direction (left becomes right and vice versa).
Take a step in your new direction.
A selection of the initial position curr and movement direction is considered valid if every element in nums becomes 0 by the end of the process.
Return the number of possible valid selections.
Example 1:
Input: nums = [1,0,2,0,3]
Output: 2
Explanation:
The only possible valid selections are the following:
Choose curr = 3, and a movement direction to the left.
[1,0,2,0,3] -> [1,0,2,0,3] -> [1,0,1,0,3] -> [1,0,1,0,3] -> [1,0,1,0,2] -> [1,0,1,0,2] -> [1,0,0,0,2] -> [1,0,0,0,2] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,0].
Choose curr = 3, and a movement direction to the right.
[1,0,2,0,3] -> [1,0,2,0,3] -> [1,0,2,0,2] -> [1,0,2,0,2] -> [1,0,1,0,2] -> [1,0,1,0,2] -> [1,0,1,0,1] -> [1,0,1,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [0,0,0,0,0].
Example 2:
Input: nums = [2,3,4,0,4,1,0]
Output: 0
Explanation:
There are no possible valid selections.
"""
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        zero_indices = [i for i, num in enumerate(nums) if num == 0]
        valid_selections = 0

        for start in zero_indices:
            for direction in [-1, 1]:  # -1 for left, 1 for right
                curr = start
                nums_copy = nums[:]
                while 0 <= curr < n:
                    if nums_copy[curr] == 0:
                        curr += direction
                    else:
                        nums_copy[curr] -= 1
                        direction *= -1
                        curr += direction
                if all(num == 0 for num in nums_copy):
                    valid_selections += 1

        return valid_selections