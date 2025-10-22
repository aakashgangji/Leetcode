"""
You are given an integer array nums and two integers k and numOperations.
You must perform an operation numOperations times on nums, where in each operation you:
Select an index i that was not selected in any previous operations.
Add an integer in the range [-k, k] to nums[i].
Return the maximum possible frequency of any element in nums after performing the operations.
Example 1:
Input: nums = [1,4,5], k = 1, numOperations = 2
Output: 2
Explanation:
We can achieve a maximum frequency of two by:
Adding 0 to nums[1], after which nums becomes [1, 4, 5].
Adding -1 to nums[2], after which nums becomes [1, 4, 4].
Example 2:
Input: nums = [5,11,20,20], k = 5, numOperations = 1
Output: 2
Explanation:
We can achieve a maximum frequency of two by:
Adding 0 to nums[1].
"""
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        # Count frequency of each number in the original array
        frequency_count = defaultdict(int)
      
        # Difference array to track range contributions
        # For each number x, we can change it to any value in [x-k, x+k]
        difference_array = defaultdict(int)
      
        for num in nums:
            # Count original frequency
            frequency_count[num] += 1
          
            # Initialize difference array entry for this number
            difference_array[num] += 0
          
            # Mark the range [num - k, num + k] where this number can contribute
            # +1 at the start of the range
            difference_array[num - k] += 1
            # -1 after the end of the range
            difference_array[num + k + 1] -= 1
      
        max_frequency = 0
        cumulative_sum = 0
      
        # Process points in sorted order to calculate maximum possible frequency
        for value, delta in sorted(difference_array.items()):
            # Update cumulative sum (number of elements that can be changed to current value)
            cumulative_sum += delta
          
            # Maximum frequency at this value is:
            # - Original count plus operations (limited by numOperations)
            # - Cannot exceed total available elements that can reach this value
            max_frequency = max(
                max_frequency, 
                min(cumulative_sum, frequency_count[value] + numOperations)
            )
      
        return max_frequency