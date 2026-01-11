"""Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
"""
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0      
        num_cols = len(matrix[0])
        heights = [0] * num_cols
        max_area = 0
        for row in matrix:
            for col_idx, value in enumerate(row):
                if value == "1":
                    heights[col_idx] += 1
                else:
                    heights[col_idx] = 0          
            max_area = max(max_area, self.largestRectangleArea(heights))
      
        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 0:
            return 0
        left_boundaries = [-1] * n  
        right_boundaries = [n] * n  
        stack = []
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] >= height:
                stack.pop()
            if stack:
                left_boundaries[i] = stack[-1]
            stack.append(i)
        stack = []
        for i in range(n - 1, -1, -1):
            height = heights[i]
            while stack and heights[stack[-1]] >= height:
                stack.pop()
            if stack:
                right_boundaries[i] = stack[-1]
            stack.append(i)
        max_area = max(
            height * (right_boundaries[i] - left_boundaries[i] - 1) 
            for i, height in enumerate(heights)
        )
        return max_area
s=Solution()
print(s.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))  # Output: 6       
