class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        dfs = [root]

        while dfs:
            node = dfs.pop()

            node.left, node.right = node.right, node.left

            if node.left:
                dfs.append(node.left)
            if node.right:
                dfs.append(node.right)
        
        return root