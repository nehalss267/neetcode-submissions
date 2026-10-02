class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result=[]
        
        if(len(result)==2*n):
            return result

        def backtrack(current_string,open_count,closed_count):
            if(open_count<n):
                backtrack(current_string+'(',open_count+1,closed_count)
            
            if(closed_count<open_count):
                backtrack(current_string+')',open_count,closed_count+1)

            if(open_count==n and closed_count==n):
                result.append(current_string)
                return
        
        backtrack("",0,0)

        return result
        