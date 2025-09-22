"""
You are given an array nums consisting of positive integers.
Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
The frequency of an element is the number of occurrences of that element in the array.
Example 1:
Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.
Example 2:
Input: nums = [1,2,3,4,5]
Output: 5
Explanation: All elements of the array have a frequency of 1 which is the maximum.
So the number of elements in the array with maximum frequency is 5.
"""
from collections import Counter

def total_frequency_of_max_frequency_elements(nums):
    freq = Counter(nums)  # Count frequency of each element
    max_freq = max(freq.values())  # Find maximum frequency
    # Sum frequencies of elements whose frequency is max_freq
    total = sum(count for count in freq.values() if count == max_freq)
    return total

# Example usage
nums1 = [1, 2, 2, 3, 1, 4]
nums2 = [1, 2, 3, 4, 5]

print(total_frequency_of_max_frequency_elements(nums1))  
print(total_frequency_of_max_frequency_elements(nums2)) 
