# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None
        #pre- rootlr 1234
        #in- lrootr 2134

        #global preorder index
        self.pre_idx=0
        indicesInorder={val:idx for idx,val in enumerate(inorder)}
        def dfs(l,r):
            if l>r:
                return None
            root_val=preorder[self.pre_idx]
            #increment pre_idx
            self.pre_idx+=1
            root=TreeNode(root_val)
            mid=indicesInorder[root_val]
            root.left=dfs(l,mid-1)
            root.right=dfs(mid+1,r)
            return root
        
        return dfs(0,len(preorder)-1)

        #visiting every node
        #t(n)=o(n)
        #s(n)=o(n)
        

        
