class Solution:
    def encode(self, strs: List[str]) -> str:
        #put delimiter len of string during string start
        res=""
        for s in strs:
            res+=str(len(s))
            res+='#'
            res+=s
        return res

    def decode(self, s: str) -> List[str]:
        resList=list()
        # reset to index
        # for index,char in enumerate(s):
        index=0
        while index<len(s):
            lenStr=0
            indx=index
            char=s[index]
            if char.isdigit():
                lenStrinStr=0
                while indx<len(s) and s[indx].isdigit():
                    lenStrinStr+=1
                    print(lenStrinStr)
                    indx+=1
                lenStr=int(s[index:indx])
                resStr=""
                resStr+=s[indx+1:(indx+1+lenStr)] 
                resList.append(resStr)
                index=index+lenStrinStr+1+lenStr
        return resList


