class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sorting according to start times
        intervals.sort(key=lambda x: x[0])
        ans=[intervals[0]]
        for start,end in intervals:
            # current start>=earliest end -> merge
            if start<=ans[-1][1]:
                ans[-1][1]=max(ans[-1][1],end)
            else:
                ans.append([start,end])
        return ans

        # t(n)=O(nlogn)
        # s(n)=0(n)
            
