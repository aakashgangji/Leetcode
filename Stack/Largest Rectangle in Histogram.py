# You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.
# Return the area of the largest rectangle that can be formed among the bars.
# Note: This chart is known as a histogram.
# Example 1:
# Input: heights = [7,1,7,2,2,4]
# Output: 8
# Example 2:
# Input: heights = [1,3,7]
# Output: 7
from typing import List
def largestRectangleArea(self, heights: List[int]) -> int:
    stack=[]
    maxa=0

    for i,h in enumerate(heights):
        start=i
        while stack and stack[-1][1]>h:
            index,height=stack.pop()
            maxa=max(maxa,height*(i-index))
            start=index

        stack.append((start,h))

    for i,h in stack:
        maxa=max(maxa,h*(len(heights)-i))
    return maxa

heights=[2,1,5,6,2,3]
print(largestRectangleArea(None,heights))