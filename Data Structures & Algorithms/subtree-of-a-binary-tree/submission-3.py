# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if the subRoot is none, it is a child of any tree, bc a None tree will have None, every other tree will have terminal None roots
        if not subRoot:
            return True
        # if we reach the root being None, but the subRoot isn't none (obv bc we never traverse it and we check right away if this is the case), then this is another base case
        if not root:
            return False
        # if curr root and given subroot is same at this node, then we have our succesful base case
        if self.sameTree(root, subRoot):
            return True
        # recurse left and right children of current node
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    # is same tree?
    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)

        return False