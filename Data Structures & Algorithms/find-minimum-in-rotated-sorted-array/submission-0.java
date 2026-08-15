class Solution {
    public int findMin(int[] a) {
        int lo=0;
        int hi=a.length-1;
        while(hi>lo){
            int mid=lo+(hi-lo)/2;
            if(a[mid]>a[hi]){
                lo=mid+1;
            }
            else{
                hi=mid;
            }
        }
        //ends when hi==lo
        return a[lo];

    }
}
