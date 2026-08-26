# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #create bounds min and max to test if any invalid node at a point
        #min is left and max is right
        #in left subtree left is bounded as min, and current node is max
        def isValidWithBounds(node,left,right):
            if node is None:
                return True #reached end(leaf) so true
            if not(left<node.val<right):
                return False #strictly less than left and greater than right -> not valid here
            return isValidWithBounds(node.left,left,node.val) and isValidWithBounds(node.right,node.val,right)

        # long used instead of int : because values can be int_max or int_min
        return isValidWithBounds(root,float('-inf'),float('inf'))
        