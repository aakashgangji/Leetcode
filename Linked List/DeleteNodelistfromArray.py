"""
You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.
Example 1:
Input: nums = [1,2,3], head = [1,2,3,4,5]
Output: [4,5]
Explanation:
Remove the nodes with values 1, 2, and 3.
Example 2:
Input: nums = [1], head = [1,2,1,2,1,2]
Output: [2,2,2]
Explanation:
Remove the nodes with value 1.
Example 3:
Input: nums = [5], head = [1,2,3,4]
Output: [1,2,3,4]
Explanation:
No node has value 5.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Convert nums list to set for O(1) lookup time
        values_to_remove = set(nums)
      
        # Create a dummy node pointing to head to handle edge cases
        # (e.g., when the head itself needs to be removed)
        dummy_node = ListNode(next=head)
      
        # Initialize pointer to traverse the list
        current = dummy_node
      
        # Traverse the linked list
        while current.next:
            # Check if the next node's value should be removed
            if current.next.val in values_to_remove:
                # Skip the next node by updating the pointer
                current.next = current.next.next
            else:
                # Move to the next node if no removal is needed
                current = current.next
      
        # Return the head of the modified list
        return dummy_node.next