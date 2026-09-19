class Solution:
    def numDecodings(self, s: str) -> int:
        # dp stores how many ways i can decode with index i
        # memoization

        # reached len(s) index from index 0-> so 1 way to decode it
        dp={len(s):1}

        # explore every index
        def dfs(i):
            if i==len(s):
                return 1
            if s[i]=="0":
                return 0
            if i in dp:
                return dp[i]
            res=dfs(i+1)
            if (i+1)<len(s) and (s[i]=="1" or (s[i]=="2" and s[i+1] in "0123456")):
                res+=dfs(i+2)
            dp[i]=res
            return res
            
        return dfs(0)
        # t(n)=o(n)
        # s(n)=o(n)