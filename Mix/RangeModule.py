"""
A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as half-open intervals and query about them.

A half-open interval [left, right) denotes all the real numbers x where left <= x < right.

Implement the RangeModule class:

RangeModule() Initializes the object of the data structure.
void addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.
boolean queryRange(int left, int right) Returns true if every real number in the interval [left, right) is currently being tracked, and false otherwise.
void removeRange(int left, int right) Stops tracking every real number currently being tracked in the half-open interval [left, right).
 

Example 1:

Input
["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
[[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
Output
[null, null, null, true, false, true]

Explanation
RangeModule rangeModule = new RangeModule();
rangeModule.addRange(10, 20);
rangeModule.removeRange(14, 16);
rangeModule.queryRange(10, 14); // return True,(Every number in [10, 14) is being tracked)
rangeModule.queryRange(13, 15); // return False,(Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
rangeModule.queryRange(16, 17); // return True, (The number 16 in [16, 17) is still being tracked, despite the remove operation)
"""
from bisect import bisect_left, bisect_right
from typing import List
class RangeModule:
    def __init__(self):
        # List of disjoint intervals, each represented as [start, end)
        self.intervals = []
    
    def addRange(self, left: int, right: int) -> None:
        newIntervals = []
        i = 0
        n = len(self.intervals)
        # Add intervals that come completely before the new interval.
        while i < n and self.intervals[i][1] < left:
            newIntervals.append(self.intervals[i])
            i += 1
        
        # Merge overlapping intervals.
        while i < n and self.intervals[i][0] <= right:
            left = min(left, self.intervals[i][0])
            right = max(right, self.intervals[i][1])
            i += 1
        newIntervals.append([left, right])
        
        # Add the remaining intervals.
        while i < n:
            newIntervals.append(self.intervals[i])
            i += 1
        
        self.intervals = newIntervals

    def queryRange(self, left: int, right: int) -> bool:
        # Use binary search to find the rightmost interval with start <= left.
        i = bisect.bisect_right(self.intervals, [left, float('inf')]) - 1
        if i < 0:
            return False
        return self.intervals[i][0] <= left and self.intervals[i][1] >= right

    def removeRange(self, left: int, right: int) -> None:
        newIntervals = []
        i = 0
        n = len(self.intervals)
        # Add intervals that come completely before [left, right).
        while i < n and self.intervals[i][1] <= left:
            newIntervals.append(self.intervals[i])
            i += 1
        
        # Adjust intervals that overlap with [left, right)
        while i < n and self.intervals[i][0] < right:
            if self.intervals[i][0] < left:
                newIntervals.append([self.intervals[i][0], left])
            if self.intervals[i][1] > right:
                newIntervals.append([right, self.intervals[i][1]])
            i += 1
        
        # Add the remaining intervals.
        while i < n:
            newIntervals.append(self.intervals[i])
            i += 1
        
        self.intervals = newIntervals


        