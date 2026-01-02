
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        numset=set()
        x=0
        for n in nums:
            if n in numset:
                return n
            numset.add(n)
            n+=1

