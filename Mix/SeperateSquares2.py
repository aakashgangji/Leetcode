"""You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.

Find the minimum y-coordinate value of a horizontal line such that the total area covered by squares above the line equals the total area covered by squares below the line.

Answers within 10-5 of the actual answer will be accepted.

Note: Squares may overlap. Overlapping areas should be counted only once in this version.

 

Example 1:

Input: squares = [[0,0,1],[2,2,1]]

Output: 1.00000

Explanation:



Any horizontal line between y = 1 and y = 2 results in an equal split, with 1 square unit above and 1 square unit below. The minimum y-value is 1.

Example 2:

Input: squares = [[0,0,2],[1,1,1]]

Output: 1.00000

Explanation:



Since the blue square overlaps with the red square, it will not be counted again. Thus, the line y = 1 splits the squares into two equal parts.
"""
from typing import List
import bisect

class SegmentTree:
    def __init__(self, xs: List[int]):
        self.xs = xs
        self.n = len(xs) - 1
        self.covered_count = [0] * (4 * self.n)
        self.covered_width = [0] * (4 * self.n)

    def add(self, i: int, j: int, val: int):
        self._add(0, 0, self.n - 1, i, j, val)

    def get_covered_width(self) -> int:
        return self.covered_width[0]

    def _add(self, tree_index: int, lo: int, hi: int, i: int, j: int, val: int):
        if j <= self.xs[lo] or self.xs[hi + 1] <= i:
            return
        if i <= self.xs[lo] and self.xs[hi + 1] <= j:
            self.covered_count[tree_index] += val
        else:
            mid = (lo + hi) // 2
            self._add(2 * tree_index + 1, lo, mid, i, j, val)
            self._add(2 * tree_index + 2, mid + 1, hi, i, j, val)

        if self.covered_count[tree_index] > 0:
            self.covered_width[tree_index] = self.xs[hi + 1] - self.xs[lo]
        elif lo == hi:
            self.covered_width[tree_index] = 0
        else:
            self.covered_width[tree_index] = (
                self.covered_width[2 * tree_index + 1]
                + self.covered_width[2 * tree_index + 2]
            )


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []  # (y, delta, xl, xr)
        xs_set = set()

        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
            xs_set.update([x, x + l])

        xs = sorted(xs_set)
        events.sort()

        half_area = self._get_area(events, xs) / 2.0
        area = 0
        prev_y = 0
        tree = SegmentTree(xs)

        for y, delta, xl, xr in events:
            covered_width = tree.get_covered_width()
            area_gain = covered_width * (y - prev_y)

            if area + area_gain >= half_area:
                # Interpolate the exact y position
                return prev_y + (half_area - area) / covered_width

            area += area_gain
            tree.add(xl, xr, delta)
            prev_y = y

        raise RuntimeError("Unexpected error")

    def _get_area(self, events, xs):
        total_area = 0
        prev_y = 0
        tree = SegmentTree(xs)
        for y, delta, xl, xr in events:
            total_area += tree.get_covered_width() * (y - prev_y)
            tree.add(xl, xr, delta)
            prev_y = y
        return total_area
s= Solution()
print(s.separateSquares([[0,0,1],[2,2,1]]))
print(s.separateSquares([[0,0,2],[1,1,1]]))
