
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        int sum = 0;
        int[] result = new int[2];
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                sum = nums[i] + nums[j];
                if (sum == target) {
                    result[0] = i;
                    result[1] = j;
                    break;
                }
            }
        }
        return result;
    }
    }

