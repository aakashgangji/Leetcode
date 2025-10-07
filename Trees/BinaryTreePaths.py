"""
Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.
Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:
Input: root = [1]
Output: ["1"]
"""
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        result = []
        
        def dfs(node, path):
            if not node:
                return
            
            path.append(str(node.val))
            
            if not node.left and not node.right:
                result.append("->".join(path))
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            
            path.pop()
        
        dfs(root, [])
        return result