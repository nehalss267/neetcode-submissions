# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        queuep=deque([p])
        queueq=deque([q])

        while queuep and queueq:
            nodep=queuep.popleft()
            nodeq=queueq.popleft()
            if nodep.val!=nodeq.val:
                return False
            if nodep.left and nodep.right:
                queuep.append(nodep.left)
                queuep.append(nodep.right)
            elif nodep.left and not nodep.right:
                queuep.append(nodep.left)
                queuep.append(TreeNode(101))
            elif nodep.right and not nodep.left:
                queuep.append(TreeNode(101))
                queuep.append(nodep.right)

            if nodeq.left and nodeq.right:
                queueq.append(nodeq.left)
                queueq.append(nodeq.right)
            elif nodeq.left and not nodeq.right:
                queueq.append(nodeq.left)
                queueq.append(TreeNode(101))
            elif nodeq.right and not nodeq.left:
                queueq.append(TreeNode(101))
                queueq.append(nodeq.right)



        return True if not queuep and not queueq else False
