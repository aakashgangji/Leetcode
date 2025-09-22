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

print(total_frequency_of_max_frequency_elements(nums1))  # Output: 4
print(total_frequency_of_max_frequency_elements(nums2))  # Output: 5
