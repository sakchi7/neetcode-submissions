# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res
        dq = deque()
        dq.append(root)
        while dq:
            l = len(dq)
            while l:
                if l == 1:
                    res.append(dq[0].val)
                vl = dq.popleft()
                if vl.left:
                    dq.append(vl.left)
                if vl.right:
                    dq.append(vl.right)
                l -= 1
        return res
        