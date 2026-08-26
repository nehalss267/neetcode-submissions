# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if any node (root,p,q) is none(null)
        if not root or not p or not q:
            return None
        # if on left side (both are less than root)
        if p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        # else if on right side (both are greater than root)
        elif p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        # else on opposite side not on 1 side (left or right)
        else:
            return root
        #O(h) :height can be logn(best) or n(worst case complexity)
        #recursive stack -s(n)=o(h)
        