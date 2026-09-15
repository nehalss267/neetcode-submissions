# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    # dfs -> explore each node not level order
    def isSameTree(self,p: Optional[TreeNode], q: Optional[TreeNode])->bool:
        if not p and not q:
            return True
        if p and q and p.val==q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        # empty is always subtree
        if not subRoot:
            return True
        # subroot not empty but root empty
        if not root:
            return False
        if self.isSameTree(root,subRoot):
            return True
        # recursively check if root.left or root.right is same as subroot
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    # visits every node of both trees
    # t(n)=o(m*n)
    # s(n)=o(m+n)
        