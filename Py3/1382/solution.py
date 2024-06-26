# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Helper function to perform inorder traversal and store elements in a list
        def inorder_traversal(node):
            if node is None:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
        
        # Helper function to construct a balanced BST from sorted array
        def sorted_array_to_bst(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = sorted_array_to_bst(nums[:mid])
            root.right = sorted_array_to_bst(nums[mid+1:])
            return root
        
        # Get the sorted elements of the BST
        sorted_elements = inorder_traversal(root)
        # Construct and return the balanced BST
        return sorted_array_to_bst(sorted_elements)
