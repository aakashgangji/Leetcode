"""
Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.
Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.
Return the minimum time Bob needs to make the rope colorful.
Example 1:
Input: colors = "abaac", neededTime = [1,2,3,4,5]
Output: 3
Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
Bob can remove the blue balloon at index 2. This takes 3 seconds.
There are no longer two consecutive balloons of the same color. Total time = 3.
Example 2:
Input: colors = "abc", neededTime = [1,2,3]
Output: 0
Explanation: The rope is already colorful. Bob does not need to remove any balloons from the rope.
Example 3:
Input: colors = "aabaa", neededTime = [1,2,3,4,1]
Output: 2
Explanation: Bob will remove the balloons at indices 0 and 4. Each balloons takes 1 second to remove.
There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.
"""
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_cost = 0
        current_index = 0
        n = len(colors)
      
        # Process groups of consecutive balloons with the same color
        while current_index < n:
            # Start of a new group
            group_start = current_index
            group_sum = 0
            max_time = 0
          
            # Find all consecutive balloons with the same color
            while current_index < n and colors[current_index] == colors[group_start]:
                # Add current balloon's removal time to group sum
                group_sum += neededTime[current_index]
                # Track the maximum removal time in this group
                if max_time < neededTime[current_index]:
                    max_time = neededTime[current_index]
                current_index += 1
          

            if current_index - group_start > 1:
                total_cost += group_sum - max_time
      
        return total_cost