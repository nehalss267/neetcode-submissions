class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> map=new HashMap<>();
        for(int i=0;i<nums.length;i++){
            int diff=target-nums[i];
            if(map.containsKey(nums[i]) && map.get(nums[i])!=i)return new int[]{map.get(nums[i]),i};//4
           //ind(4) 
            map.put(diff,i);//ind(3) 4 //

            //4 
        }
        return new int[]{};
    }
}
