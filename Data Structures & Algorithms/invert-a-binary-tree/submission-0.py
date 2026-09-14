# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # BFS (level order traversal)

        # putting root in queue
        queue=deque([root])
        # till queue is not empty, popping leftest nodes in queue (FIFO), inverting nodes(node.left,node.right=node.right,node.left), checking if they have left node (push it) and then right node (push it). thus iterating through all nodes
        while queue:
            node=queue.popleft()
            # inverting
            node.left,node.right=node.right,node.left
            # appending child nodes
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root

        # t(n)=o(n)
        # s(n)=o(n)