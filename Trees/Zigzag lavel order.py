# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
