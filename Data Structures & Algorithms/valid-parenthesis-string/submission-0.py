class Solution:
    def checkValidString(self, s: str) -> bool:
        # count open and closed paranthesis from both ends simultanously (2 pointers) 
        # count open in froward direction starting from 0 : add 1 if open count or * present,
        # else subtract 1 
        # count closed in reverse direction starting from end: add 1 if closed or * present,  else subtract 1
        # if at any point, open_cnt or close_cnt is negative : invalid paranthesis
        open_cnt=close_cnt=0 
        length=len(s)-1
        for i in range(len(s)):
            
            if s[i]=='(' or s[i]=='*':
                open_cnt+=1
            else:
                open_cnt-=1
            
            if s[length-i]==')' or s[length-i]=='*':
                close_cnt+=1
            else:
                close_cnt-=1

            if open_cnt<0 or close_cnt<0:
                return False
        return True