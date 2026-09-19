class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        len1=len(s)
        for i in range(0,len1+1):
            for j in range(i):
                substr=s[j:i]
                if s[j:i]==substr[::-1]:
                    if len(res)<len(substr):
                        res=substr
        return res