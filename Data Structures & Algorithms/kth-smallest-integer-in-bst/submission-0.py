# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        heap=[]
        queue=deque([root])
        while queue:
            node=queue.popleft()
            heapq.heappush(heap,node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        heap.sort()
        print(heap)
        return heap[k-1]