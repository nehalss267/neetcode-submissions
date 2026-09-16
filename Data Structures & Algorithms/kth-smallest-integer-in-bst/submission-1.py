# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder - t(n)=o(n), s(n)=o(n)
        # morris traversal - t(n)=o(n), s(n)=o(1) -simulates inorder at each step k-- , when k=0, reached desired node
        if not root:
            return 0
        arr=[]
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        inorder(root)
        return arr[k-1] 
        


            

        