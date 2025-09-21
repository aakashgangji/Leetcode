"""
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.
Example 1:
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:
Input: head = []
Output: []
"""
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        def build(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(values[mid])
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root
        
        return build(0, len(values) - 1)