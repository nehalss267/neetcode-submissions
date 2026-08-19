class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit=Integer.MIN_VALUE;
        int minPrice=Integer.MAX_VALUE;
        for(int sell: prices){
            minPrice=Math.min(minPrice,sell);
            maxProfit=Math.max(maxProfit,sell-minPrice);
        }
        return maxProfit;
    }
}
