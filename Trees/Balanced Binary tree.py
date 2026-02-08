# Given a binary tree, determine if it is height-balanced.

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:

# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root: return [True,0]

            left,right=dfs(root.left),dfs(root.right)
            balanced=(left[0] and right[0] and (abs(left[1]-right[1])<=1))
            return balanced,1+max(left[1],right[1])
        return dfs(root)[0]
#or
"""class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            left=dfs(root.left)
            if left==-1:
                return -1
            right=dfs(root.right)
            if right==-1:
                return -1
            if abs(left-right)>1:
                return -1
            return 1+max(left,right)
        return dfs(root)!=-1
"""
s=Solution()
print(s.isBalanced([3,9,20,None,None,15,7]))  # True
print(s.isBalanced([1,2,2,3,3,None,None,4,4]))  # False
print(s.isBalanced([]))  # True 
    
    