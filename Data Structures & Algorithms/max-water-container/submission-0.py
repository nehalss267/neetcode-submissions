class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lt=0
        rt=len(heights)-1
        maxlen=-float("inf")
        maxarea=-float("inf")
        while rt>lt:
            if(heights[rt]>=heights[lt]):
                maxlen=rt-lt
                maxarea=max(maxarea,maxlen*min(heights[lt],heights[rt]))
                lt+=1
            else:
                maxlen=rt-lt
                maxarea=max(maxarea,maxlen*min(heights[lt],heights[rt]))
                rt-=1
        return maxarea