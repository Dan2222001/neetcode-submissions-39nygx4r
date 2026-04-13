# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        balanced = True

        def DFS(root: Optional[TreeNode]) -> int:
            nonlocal balanced
            if root is None:
                return 0
            
            else:
                diff = DFS(root.left) - DFS(root.right)
                if diff > 1 or diff < -1:
                    balanced = False
                return max(DFS(root.left), DFS(root.right)) + 1
            
        DFS(root)
        return balanced