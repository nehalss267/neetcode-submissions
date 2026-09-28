class Solution:
    def maxDepth(self, s: str) -> int:
        ans=0
        stackPar=[]
        for c in s:
            if c=='(':
                stackPar.append(c)
            elif c==')':
                stackPar.pop()
            ans=max(ans,len(stackPar))
        return ans
        