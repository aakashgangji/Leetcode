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

Since k == x, answer[i] is equal to the sum of the subarray nums[i..i + k - 1].

"""
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def add_element_to_sets(value: int) -> None:
            """Add an element to either top_x_elements or remaining_elements based on priority."""
            if element_count[value] == 0:
                return
          
            # Create priority tuple (frequency, value) for comparison
            priority_tuple = (element_count[value], value)
          
            # If top set is empty or new element has higher priority than minimum in top set
            if top_x_elements and priority_tuple > top_x_elements[0]:
                nonlocal current_sum
                current_sum += priority_tuple[0] * priority_tuple[1]  # frequency * value
                top_x_elements.add(priority_tuple)
            else:
                remaining_elements.add(priority_tuple)
      
        def remove_element_from_sets(value: int) -> None:
            """Remove an element from either top_x_elements or remaining_elements."""
            if element_count[value] == 0:
                return
          
            priority_tuple = (element_count[value], value)
          
            if priority_tuple in top_x_elements:
                nonlocal current_sum
                current_sum -= priority_tuple[0] * priority_tuple[1]  # frequency * value
                top_x_elements.remove(priority_tuple)
            else:
                remaining_elements.remove(priority_tuple)
      
        # Initialize data structures
        top_x_elements = SortedList()      # Stores top x frequent elements
        remaining_elements = SortedList()   # Stores remaining elements
        element_count = Counter()           # Tracks frequency of each element
        current_sum = 0                     # Current x-sum
        n = len(nums)
        result = [0] * (n - k + 1)         # Result array for all windows
      
        # Process each element
        for i, current_value in enumerate(nums):
            # Update element in the window
            remove_element_from_sets(current_value)
            element_count[current_value] += 1
            add_element_to_sets(current_value)
          
            # Calculate window start index
            window_start = i - k + 1
          
            # Skip if window is not complete yet
            if window_start < 0:
                continue
          
            # Balance the sets: ensure top_x_elements has exactly x elements
            # Move elements from remaining_elements to top_x_elements if needed
            while remaining_elements and len(top_x_elements) < x:
                element_to_promote = remaining_elements.pop()
                top_x_elements.add(element_to_promote)
                current_sum += element_to_promote[0] * element_to_promote[1]
          
            # Move excess elements from top_x_elements to remaining_elements
            while len(top_x_elements) > x:
                element_to_demote = top_x_elements.pop(0)
                current_sum -= element_to_demote[0] * element_to_demote[1]
                remaining_elements.add(element_to_demote)
          
            # Store the x-sum for current window
            result[window_start] = current_sum
          
            # Remove the leftmost element from window for next iteration
            leftmost_element = nums[window_start]
            remove_element_from_sets(leftmost_element)
            element_count[leftmost_element] -= 1
            if element_count[leftmost_element] > 0:
                add_element_to_sets(leftmost_element)
      
        return result
