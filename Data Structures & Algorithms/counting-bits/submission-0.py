class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(0,n+1):
            l.append(str(bin(i)[2:]))
        li=[]
        for d in l:
            elem=0
            for c in d:
                elem+=int(c)
            li.append(elem)
        return li