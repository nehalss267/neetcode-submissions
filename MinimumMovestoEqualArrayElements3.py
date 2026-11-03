# Code

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return abs(sum(nums) - max(nums) * len(nums))
'''
# Intuition

If the goal is to make all elements equal by incrementing **one element at a time**, the most efficient target is the maximum value in the array. Every element needs to be increased until it matches this maximum value.


# Approach

Instead of iterating through the array and summing the difference for each element `(max_val - num)`, we can optimize this mathematically. The total target sum if all elements were the maximum is `max(nums) * len(nums)`. Subtracting the current `sum(nums)` from this theoretical target sum gives the exact total number of increments needed. Wrapping it in `abs()` ensures a positive integer regardless of the subtraction order.

# Complexity

* Time complexity: 
$$O(n)$$. Since these operations run sequentially(max(),sum()), the overall time complexity remains linear.

* Space complexity: 
$$O(1)$$


'''