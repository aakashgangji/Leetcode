from typing import List
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    a,b=nums1,nums2
    total=len(nums1)+len(nums2)
    half=total//2

    if len(b)<len(a):
        a,b=b,a
    l,r=0,len(a)-1
    while True:
        i=(l+r)//2
        j=half-i-2
        aleft=a[i] if i>=0 else float("-infinity")
        aright=a[i+1] if (i+1)<len(a) else float("infinity")
        bleft=b[j] if j>=0 else float ("-infinity")
        bright=b[j+1] if (j+1)<len(b) else float("infinity")

        if aleft<=bright and bleft<=aright:
            if total%2:
                return min(aright,bright)
            return (max(aleft,bleft)+min(aright,bright))/2
        
        elif aleft>bright:
            r=i-1
        else:
            l=i+1

nums1 = [1,2]
nums2 = [3,4]
print(findMedianSortedArrays(None, nums1, nums2))  
