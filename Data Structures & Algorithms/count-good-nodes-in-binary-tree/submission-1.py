# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        if root is None:
            return res
        dq = deque([(root, -111)])
        while dq:
            vl, curr  = dq.popleft()
            if vl.val >= curr:
                res += 1
            if vl.left:
                dq.append((vl.left, max(curr, vl.val)))
            if vl.right:
                dq.append((vl.right, max(curr, vl.val)))
        return res
        