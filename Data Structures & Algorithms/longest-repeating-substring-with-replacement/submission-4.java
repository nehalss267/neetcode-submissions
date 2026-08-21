class Solution {
    public int characterReplacement(String s, int k) {
        //XYYX
        //2 ->2 Y replaced with X //2 can be atmost k
        //maximize sliding window 
        //longest window (ensure window: with same char)-> longest substring
        //replace all char in window with c (# of such char=window size-count of c already present )
        int max=Integer.MIN_VALUE;
        Set<Character> charSet=new HashSet<>();
        for(char c:s.toCharArray()){
            charSet.add(c);
        }
        //s.toCharArray() use instead of set ,gives tle(o(n*m);n=#charArray elem) error we just wnat disticnt char(no duplicates) so use set
        for(char c:charSet){
            //initialize window
            int l=0;
            int count=0;//cnt of c
            for(int r=0;r<s.length();r++){
                if(s.charAt(r)==c){
                    count++;
                }
        //replace all char in window with c (# of such char=window size-count of c already present )
        //if exceeds then l++ (reduce window size)
                while((r-l+1)-count>k){
                    if(s.charAt(l)==c){
                        count--;
                    }
                    l++;
                }
  
                max=Math.max((r-l+1),max);

            }
        }
        return max;
    }
}
