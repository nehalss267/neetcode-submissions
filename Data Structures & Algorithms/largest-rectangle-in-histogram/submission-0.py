class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 2 arrays - leftmost, rightmost - stores index of nearest strictly smaller height on left of index i and right of index i resp.
        # 1 monotonic stack - stores candidate indices whose nearest smallest elements haven't been found yet
        # for leftmost : forward pass - initialize as -1
        # for rightmost : reverse pass  - initialize as len(heights)
        n=len(heights)
        leftmost=[-1]*n
        rightmost=[n]*n
        stack=[]
        # forward pass
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                leftmost[i]=stack[-1]
            stack.append(i)

        # reverse pass : reinitialiaze stack
        stack=[] # very important
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                rightmost[i]=stack[-1]
            stack.append(i)

        maxArea=0
        for i in range(n):
            # correcting 0 indexing
            leftmost[i]+=1
            rightmost[i]-=1
            # area=height*width
            maxArea=max(maxArea,heights[i]*(rightmost[i]-leftmost[i]+1))
        return maxArea



            


