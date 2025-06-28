from typing import List
def rob(self, nums: List[int]) -> int:
    r1,r2=0,0
    for num in nums:
        temp=max(num+r1,r2)
        r1=r2
        r2=temp
    return r2

nums=[1,3,5,6,8,4,5,9,5]
print(rob(None,nums))
