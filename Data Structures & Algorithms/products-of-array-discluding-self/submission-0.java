class Solution {
    public int[] productExceptSelf(int[] nums) {

        int prod = 1;
        int temp = 0;
        // List<Integer> prodList = new ArrayList<>();

        int[] prodArray = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            prod = 1;
            temp = nums[i];
            for (int j = 0; j < nums.length; j++) {
                nums[i] = 1;
                prod *= nums[j];
            }
            prodArray[i] = prod;
            // prodList.add(prod);
            nums[i] = temp;
        }
        // System.out.println(prodList.toString());
        // prodList.stream().forEach(d->System.out.println(d));

        return prodArray;
    }


}
