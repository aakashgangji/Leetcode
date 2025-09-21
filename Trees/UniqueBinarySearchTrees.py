"""
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
Example 1:
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:
Input: n = 1
Output: [[1]]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n==0:
            return []
        def gen(start,end):
            if start>end:
                return [None]
            all_trees=[]
            for rootv in range(start, end+1):
                left_t=gen(start,rootv-1)
                right_t=gen(rootv+1,end)
                for left in left_t:
                    for right in right_t:
                        root=TreeNode(rootv)

                        root.left=left
                        root.right=right
                        all_trees.append(root)
            return all_trees
        return gen(1,n)