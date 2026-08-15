class Solution {
    public int findMinIndex(int[] a, int t) {
        int lo=0;
        int hi=a.length-1;
        while(hi>lo){
            int mid=lo+(hi-lo)/2;
            if(a[mid]>a[hi])lo=mid+1;
            else hi=mid;
            
        }
        return lo;
    }
    public int search(int[] a, int t) {

        int lo=0;
        int hi=a.length-1;
        int min=findMinIndex(a,t);//0
        if(a[min]<=t && t<=a[hi]){
            lo=min;
        }else{
            hi=min-1;
        }

        while(hi>=lo){
            int mid=lo+(hi-lo)/2;
            if(a[mid]>t)hi=mid-1;
            else if(a[mid]==t)return mid;
            else lo=mid+1;
            
        }
        return -1;
    }
}
