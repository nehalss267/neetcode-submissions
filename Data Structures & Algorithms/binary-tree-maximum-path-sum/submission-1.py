# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 2 values involve each node:
        # max downward sum
        # sum of path constituting this node-> returned by pathSum
        # consider -ve values: others can be added
        self.res=root.val
        def pathSum(root)->int:
            if not root:
                return 0
            leftSum=pathSum(root.left)
            rightSum=pathSum(root.right)
            # add if not -ve
            leftSum=max(leftSum,0)
            rightSum=max(rightSum,0)

            # sum of path including node
            self.res=max(self.res,root.val+leftSum+rightSum)
            # return downward sum
            return root.val+max(leftSum,rightSum)
        
        pathSum(root)
        return self.res
        

                


        