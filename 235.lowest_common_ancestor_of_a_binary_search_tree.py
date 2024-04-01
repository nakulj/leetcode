# Definition for a binary tree node.
from typing import Iterator


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        a, b = sorted([p.val, q.val])
        while not (a <= root.val <= b):
            root = root.right if root.val < a else root.left
        return root
