class Solution {
    public int characterReplacement(String s, int k) {
        //XYYX
        //2 ->2 Y replaced with X //2 can be atmost k
        //maximize sliding window 
        //longest window (ensure window: with same char)-> longest substring
        //replace all char in window with c (# of such char=window size-count of c already present )
        int max=Integer.MIN_VALUE;
        int maxf=Integer.MIN_VALUE;
        
        //s.toCharArray() use instead of set ,gives tle(o(n*m);n=#charArray elem) error we just wnat disticnt char(no duplicates) so use set
            //purpose of set was to keep track of cnt-> done by hashmap
        HashMap<Character,Integer> count=new HashMap<>();
            //initialize window
            int l=0;
            for(int r=0;r<s.length() ;r++){
                //r looping through every character of s
                count.put(s.charAt(r),count.getOrDefault(s.charAt(r),0)+1);
        //replace all char in window with c (# of such char=window size-count of c already present )
        //if exceeds then l++ (reduce window size)
                maxf=Math.max(count.get(s.charAt(r)),maxf);
                while((r-l+1)-maxf>k){
                    count.put(s.charAt(l),count.getOrDefault(s.charAt(l),0)-1);
                    l++;
                }
  
                max=Math.max((r-l+1),max);
            }
        return max;

        }
}
