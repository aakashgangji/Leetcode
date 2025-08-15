'''
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []

'''
from collections import deque
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root) -> List[List[int]]:
        if not root:
            return []

        res=[]
        queue=deque([root])
        ltr=True

        while queue:
            level=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if not ltr:
                level.reverse()
            res.append(level)
            ltr=not ltr
        return res

        def dfs(root):
            if not root:
                return res
            if root:
                res.append([root.val])
                if zig==True:
                    dfs(root.left.val)
                    dfs(root.right.val)
                    zig= False
                else:
                    dfs(root.right.val)
                    dfs(root.left.val)
                    zig=True
            zig=False
        return res

root=TreeNode(3,TreeNode(4,TreeNode(5,TreeNode(7))))

