"""
Given the roots of two binary trees p and q,
write a function to check if they are the same or not.
Two binary trees are considered the same if they are
structurally identical, and the nodes have the same value.

Understanding:
Input: p_TreeNode, q_TreeNode
Output: Boolean (TRUE/FALSE)

Match: BinaryTree problem

Edge Cases:
if no root: return True

Plan:
1.if both p and q are NONE- return True
2. if the values of the leaf nodes when compared to each other 
    are not equal- return False (both the right and left nodes of the tree)
3.recurivelly call the function again

Implement:

Review:

Evaluate:
Time complexity=O(N)
Space Complexity=O(h)
h-height of the tree
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if p and q and p.val==q.val:
        return (isSameTree(p.left,q.left) and isSameTree(p.right,q.right))
    else:
        return False
    
p=TreeNode(1,TreeNode(2))
q=TreeNode(1,TreeNode(None,TreeNode(2)))
print(isSameTree(p,q))

