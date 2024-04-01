# Definition for a binary tree node.


from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right


def children(node: TreeNode):
    return (n for n in [node.left, node.right] if n is not None)


class Solution:
    def isUnivalTree(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        val = root.val
        d = deque(children(root))
