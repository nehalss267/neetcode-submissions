
class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer, Integer> check = new HashMap<>();
        int find = 0;
        for (int value : nums) {
            if (!check.containsKey(value)) {
                find=1;
                check.put(value, find);
            } else {
                return true;
            }
        }
        return false;
    }
    
}