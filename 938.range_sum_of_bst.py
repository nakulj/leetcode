# Definition for a binary tree node.
from typing import Iterator


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def rangeSumBST(self, root:TreeNode|None, low: int, high: int) -> int:
        if root is None:
            return 0
        s = 0
        if low <= root.val <= high:
            s += root.val 
        if root.val >= low:
            s += self.rangeSumBST(root.left,low,high)
        if root.val <= high:
            s += self.rangeSumBST(root.right, low, high)
        return s
        
