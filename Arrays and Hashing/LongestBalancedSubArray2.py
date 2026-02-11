"""You are given an integer array nums.

A subarray is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers.

Return the length of the longest balanced subarray.

 

Example 1:

Input: nums = [2,5,4,3]

Output: 4

Explanation:

The longest balanced subarray is [2, 5, 4, 3].
It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [5, 3]. Thus, the answer is 4.
Example 2:

Input: nums = [3,2,2,5,4]

Output: 5

Explanation:

The longest balanced subarray is [3, 2, 2, 5, 4].
It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [3, 5]. Thus, the answer is 5.
Example 3:

Input: nums = [1,2,3,2]

Output: 3

Explanation:

The longest balanced subarray is [2, 3, 2].
It has 1 distinct even number [2] and 1 distinct odd number [3]. Thus, the answer is 3.
"""
import sys

# Increase recursion depth for deep segment tree operations
sys.setrecursionlimit(200000)

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Segment Tree arrays
        # We need min and max to quickly check if '0' exists in a range
        self.tree_min = [0] * (4 * n)
        self.tree_max = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        
        last_pos = {}
        max_len = 0
        
        # Helper to push lazy updates down to children
        def push(node):
            if self.lazy[node] != 0:
                mid = node * 2
                right = node * 2 + 1
                
                self.lazy[mid] += self.lazy[node]
                self.tree_min[mid] += self.lazy[node]
                self.tree_max[mid] += self.lazy[node]
                
                self.lazy[right] += self.lazy[node]
                self.tree_min[right] += self.lazy[node]
                self.tree_max[right] += self.lazy[node]
                
                self.lazy[node] = 0

        # Range update: add val to [l, r]
        def update(node, start, end, l, r, val):
            if l > end or r < start:
                return
            if l <= start and end <= r:
                self.tree_min[node] += val
                self.tree_max[node] += val
                self.lazy[node] += val
                return
            
            push(node)
            mid = (start + end) // 2
            update(node * 2, start, mid, l, r, val)
            update(node * 2 + 1, mid + 1, end, l, r, val)
            
            self.tree_min[node] = min(self.tree_min[node*2], self.tree_min[node*2+1])
            self.tree_max[node] = max(self.tree_max[node*2], self.tree_max[node*2+1])

        # Find the leftmost index with value 0
        def query_first_zero(node, start, end, l, r):
            # If current range is completely outside query range
            if l > end or r < start:
                return -1
            
            # Optimization: If 0 is not in the range of values [min, max], skip
            if self.tree_min[node] > 0 or self.tree_max[node] < 0:
                return -1
            
            if start == end:
                return start if self.tree_min[node] == 0 else -1
            
            push(node)
            mid = (start + end) // 2
            
            # Try left child first to find the *leftmost* index
            res = query_first_zero(node * 2, start, mid, l, r)
            if res != -1:
                return res
            
            # If not found in left, try right
            return query_first_zero(node * 2 + 1, mid + 1, end, l, r)

        for r, num in enumerate(nums):
            prev = last_pos.get(num, -1)
            
            # Determine update value: +1 for even, -1 for odd
            val = 1 if num % 2 == 0 else -1
            
            # Update the range (prev_pos + 1, current_r)
            update(1, 0, n - 1, prev + 1, r, val)
            
            # Record new last position
            last_pos[num] = r
            
            # Find leftmost L such that balance is 0
            l_opt = query_first_zero(1, 0, n - 1, 0, r)
            
            if l_opt != -1:
                max_len = max(max_len, r - l_opt + 1)
                
        return max_len
s=Solution()
print(s.longestBalanced([2,5,4,3]))
print(s.longestBalanced([3,2,2,5,4]))
print(s.longestBalanced([1,2,3,2])) 
