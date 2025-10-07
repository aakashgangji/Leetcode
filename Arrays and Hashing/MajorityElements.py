class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        f = {}
        for n in nums:
            f[n] = f.get(n, 0) + 1
        for n,count in f.items():
            if count>=len(nums)//2:
                return n
        return None