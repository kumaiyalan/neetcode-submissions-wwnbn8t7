# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def findNode(node: 'TreeNode', left: int, right: int) -> 'TreeNode':

            if left <= node.val and node.val <= right:
                return node
            
            if node.val < left:
   
                return findNode(node.right, left, right)
            
            if node.val > right:
          
                return findNode(node.left, left, right)
        
        minimum = min(p.val, q.val)
        maximum = max(p.val, q.val)

        return findNode(root, minimum, maximum)
        