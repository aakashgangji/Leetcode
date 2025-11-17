"""
Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of disjoint intervals.

Implement the SummaryRanges class:

SummaryRanges() Initializes the object with an empty stream.
void addNum(int value) Adds the integer value to the stream.
int[][] getIntervals() Returns a summary of the integers in the stream currently as a list of disjoint intervals [starti, endi]. The answer should be sorted by starti.
 

Example 1:

Input
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
Output
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

Explanation
SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1);      // arr = [1]
summaryRanges.getIntervals(); // return [[1, 1]]
summaryRanges.addNum(3);      // arr = [1, 3]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
summaryRanges.addNum(7);      // arr = [1, 3, 7]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]
"""
class SummaryRanges:
    def __init__(self):
        self.intervals = SortedDict()  
    def addNum(self, val: int) -> None:
        if val in self.intervals:
            return
        lo = self._lowerKey(val)
        hi = self._higherKey(val)
        if lo >= 0 and hi >= 0 and self.intervals[lo][1] + 1 == val and val + 1 == hi:
            self.intervals[lo][1] = self.intervals[hi][1]
            del self.intervals[hi]
        elif lo >= 0 and self.intervals[lo][1] + 1 >= val:
            self.intervals[lo][1] = max(self.intervals[lo][1], val)
        elif hi >= 0 and val + 1 == hi:
            self.intervals[val] = [val, self.intervals[hi][1]]
            del self.intervals[hi]
        else:
            self.intervals[val] = [val, val]

    def getIntervals(self) -> list[list[int]]:
        return list(self.intervals.values())

    def _lowerKey(self, key: int):
        i = self.intervals.bisect_left(key)
        if i == 0:
            return -1
        return self.intervals.peekitem(i - 1)[0]

    def _higherKey(self, key: int):
        i = self.intervals.bisect_right(key)
        if i == len(self.intervals):
            return -1
        return self.intervals.peekitem(i)[0]