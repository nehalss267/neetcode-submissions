class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lt=0
        rt=len(heights)-1
        maxarea=-float("inf")
        while rt>lt:
            width=rt-lt
            maxarea=max(maxarea,width*min(heights[lt],heights[rt]))
            if(heights[rt]>=heights[lt]):
                lt+=1
            else:
                rt-=1
        return maxarea