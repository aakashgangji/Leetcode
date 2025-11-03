"""
Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.
Example 1:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000
Explanation: The five points are shown in the above figure. The red triangle is the largest.
Example 2:
Input: points = [[1,0],[0,0],[0,1]]
Output: 0.50000
"""

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(a,b,c):
            return abs((a[0]*(b[1]-c[1])+b[0]*(c[1]-a[1])+c[0]*(a[1]-b[1]))/2)
        n=len(points)
        max_area=0
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    max_area=max(max_area,area(points[i],points[j],points[k]))
        return max_area