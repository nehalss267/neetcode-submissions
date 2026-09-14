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
            # both none so equivalent
            if not nodep and not nodeq:
                continue
            # just 1 none then not equivalent
            if not nodep or not nodeq or nodep.val!=nodeq.val:
                return False
          
            queuep.append(nodep.left)
            queuep.append(nodep.right)
            queueq.append(nodeq.left)
            queueq.append(nodeq.right)
            
        return True if not queuep and not queueq else False
        # visits every node if tree equivalent
        # t(n)=o(n)
        # s(n)=o(n)
