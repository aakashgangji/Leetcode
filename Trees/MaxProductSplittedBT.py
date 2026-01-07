"""Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
Example 2:


Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
 """
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        total_sum = 0
        subtree_sums = []

        def compute_subtree_sums(node):
            nonlocal total_sum
            if not node:
                return 0
            left_sum = compute_subtree_sums(node.left)
            right_sum = compute_subtree_sums(node.right)
            subtree_sum = node.val + left_sum + right_sum
            subtree_sums.append(subtree_sum)
            total_sum += node.val
            return subtree_sum

        compute_subtree_sums(root)

        max_product = 0
        for sub_sum in subtree_sums:
            product = sub_sum * (total_sum - sub_sum)
            max_product = max(max_product, product)

        return max_product % MOD