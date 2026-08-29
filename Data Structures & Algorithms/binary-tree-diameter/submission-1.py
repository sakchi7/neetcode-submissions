# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxHt = 0
    def subTreeHt(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftHt = self.subTreeHt(root.left)
        rightHt = self.subTreeHt(root.right)
        self.maxHt = max(self.maxHt, (leftHt + rightHt))
        return 1 + max(leftHt, rightHt)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxHt = 0
        self.subTreeHt(root)
        return self.maxHt