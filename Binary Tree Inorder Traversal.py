# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []

        def nested(node):
            if node:
                nested(node.left)
                out.append(node.val)
                nested(node.right)

        nested(root)
        return out
