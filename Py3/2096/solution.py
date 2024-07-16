# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # Helper function to find the LCA
        def findLCA(node, p, q):
            if not node:
                return None
            if node.val == p or node.val == q:
                return node
            left = findLCA(node.left, p, q)
            right = findLCA(node.right, p, q)
            if left and right:
                return node
            return left if left else right
        
        # Helper function to find the path from the current node to the target node
        def findPath(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True
            path.append('L')
            if findPath(node.left, target, path):
                return True
            path.pop()
            path.append('R')
            if findPath(node.right, target, path):
                return True
            path.pop()
            return False
        
        # Find the LCA of startValue and destValue
        lca = findLCA(root, startValue, destValue)
        
        # Find the path from the LCA to startValue and to destValue
        start_to_lca_path = []
        findPath(lca, startValue, start_to_lca_path)
        
        lca_to_dest_path = []
        findPath(lca, destValue, lca_to_dest_path)
        
        # Generate the directions string
        directions = 'U' * len(start_to_lca_path) + ''.join(lca_to_dest_path)
        return directions
