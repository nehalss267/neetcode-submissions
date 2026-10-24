class Solution:
    # merge sort: O(nlogn)
    # divides arr from left to mid-1 and from mid to right
    # then sorts these halves and merges them

    def merge(self,larr:List[int],rarr:List[int],n)->List[int]:
        sortedarr=[]
        ltptr=0
        rtptr=0
        arrptr=0
        while(ltptr<len(larr) and rtptr<len(rarr)):
            if larr[ltptr]<rarr[rtptr]:
                sortedarr.append(larr[ltptr])
                ltptr+=1
            else:
                sortedarr.append(rarr[rtptr])
                rtptr+=1
            arrptr+=1
        sortedarr.extend(larr[ltptr:])
        sortedarr.extend(rarr[rtptr:])
        return sortedarr

    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) <= 1:
            return nums
            
        mid = len(nums) // 2

        larr=self.sortArray(nums[:mid])
        rarr=self.sortArray(nums[mid:])
        return self.merge(larr,rarr,len(nums))