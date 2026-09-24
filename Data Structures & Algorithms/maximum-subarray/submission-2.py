class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algorithm
        # t(n)=O(n)
        # s(n)=O(1)
        curr_sum=nums[0]
        max_sum=nums[0]
        for r in range(1,len(nums)):
            if curr_sum<0:
                curr_sum=0
            curr_sum+=nums[r]
            max_sum=max(curr_sum,max_sum)
        return max_sum
