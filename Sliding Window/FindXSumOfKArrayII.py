"""
You are given an array nums of n integers and two integers k and x.

The x-sum of an array is calculated by the following procedure:

Count the occurrences of all elements in the array.
Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
Calculate the sum of the resulting array.
Note that if an array has less than x distinct elements, its x-sum is the sum of the array.

Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1].

 

Example 1:

Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2

Output: [6,10,12]

Explanation:

For subarray [1, 1, 2, 2, 3, 4], only elements 1 and 2 will be kept in the resulting array. Hence, answer[0] = 1 + 1 + 2 + 2.
For subarray [1, 2, 2, 3, 4, 2], only elements 2 and 4 will be kept in the resulting array. Hence, answer[1] = 2 + 2 + 2 + 4. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.
For subarray [2, 2, 3, 4, 2, 3], only elements 2 and 3 are kept in the resulting array. Hence, answer[2] = 2 + 2 + 2 + 3 + 3.
Example 2:

Input: nums = [3,8,7,8,7,5], k = 2, x = 2

Output: [11,15,15,15,12]

Explanation:

Since k == x, answer[i] is equal to the sum of the subarray nums[i..i + k - 1]
"""

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:

      
        def add_to_sets(value: int) -> None:
            """Add element to either top_x_set or remaining_set based on its priority."""
            if frequency_map[value] == 0:
                return
          
            priority_tuple = (frequency_map[value], value)
          
            # If top_x_set is empty or this element has higher priority than the minimum in top_x_set
            if top_x_set and priority_tuple > top_x_set[0]:
                nonlocal current_sum
                current_sum += priority_tuple[0] * priority_tuple[1]  # frequency * value
                top_x_set.add(priority_tuple)
            else:
                remaining_set.add(priority_tuple)
      
        def remove_from_sets(value: int) -> None:
            """Remove element from whichever set it belongs to."""
            if frequency_map[value] == 0:
                return
          
            priority_tuple = (frequency_map[value], value)
          
            if priority_tuple in top_x_set:
                nonlocal current_sum
                current_sum -= priority_tuple[0] * priority_tuple[1]  # frequency * value
                top_x_set.remove(priority_tuple)
            else:
                remaining_set.remove(priority_tuple)
      
        # Initialize data structures
        top_x_set = SortedList()      # Maintains top x elements by (frequency, value)
        remaining_set = SortedList()   # Maintains remaining elements
        frequency_map = Counter()       # Tracks frequency of each element in current window
        current_sum = 0                 # Sum of top x elements
        n = len(nums)
        result = [0] * (n - k + 1)     # Result array for each window
      
        # Process each element
        for i, current_value in enumerate(nums):
            # Update frequency for current element
            remove_from_sets(current_value)
            frequency_map[current_value] += 1
            add_to_sets(current_value)
          
            # Calculate window start index
            window_start = i - k + 1
          
            # Skip if we haven't formed a complete window yet
            if window_start < 0:
                continue
          
            # Balance the sets: ensure top_x_set has exactly x elements
            # Move elements from remaining_set to top_x_set if needed
            while remaining_set and len(top_x_set) < x:
                element = remaining_set.pop()
                top_x_set.add(element)
                current_sum += element[0] * element[1]
          
            # Move excess elements from top_x_set to remaining_set
            while len(top_x_set) > x:
                element = top_x_set.pop(0)  # Remove smallest element
                current_sum -= element[0] * element[1]
                remaining_set.add(element)
          
            # Store result for current window
            result[window_start] = current_sum
          
            # Remove the leftmost element of the window for next iteration
            leftmost_element = nums[window_start]
            remove_from_sets(leftmost_element)
            frequency_map[leftmost_element] -= 1
            if frequency_map[leftmost_element] > 0:
                add_to_sets(leftmost_element)
      
        return result