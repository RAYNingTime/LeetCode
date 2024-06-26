# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
            def reverse_in_order_traversal(node, acc_sum):
                if not node:
                    return acc_sum
                # Traverse the right subtree
                acc_sum = reverse_in_order_traversal(node.right, acc_sum)
                # Update the node's value
                acc_sum += node.val
                node.val = acc_sum
                # Traverse the left subtree
                acc_sum = reverse_in_order_traversal(node.left, acc_sum)
                return acc_sum
            
            reverse_in_order_traversal(root, 0)
            return root
