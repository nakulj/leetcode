# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root:TreeNode)->TreeNode:
    tail = root
    l, r = root.left, root.right
    if l:
        root.left = None
        root.right = l
        tail = flatten(l)
    if r:
        tail.right = r
        tail = flatten(r)
    return tail


class Solution:
    def flatten(self, root:TreeNode|None) -> None:
        if root:
            flatten(root)
        """
        Do not return anything, modify root in-place instead.
        """
        
