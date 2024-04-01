# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:

    def __init__(self, root:TreeNode):
        self.root = root
        self.q:list[TreeNode] = [root]
        while True:
            n = self.q[0]
            if n.left is None:
                return
            self.q.append(n.left)
            if n.right is None:
                return
            self.q.append(n.right)
            self.q.pop(0)



    def insert(self, val: int) -> int:
        new = TreeNode(val)
        n = self.q[0]
        if n.left is None:
            n.left = new
        elif n.right is None:
            n.right = new
            self.q.pop(0)
        self.q.append(new)
        return n.val
        

    def get_root(self) ->TreeNode|None:
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
