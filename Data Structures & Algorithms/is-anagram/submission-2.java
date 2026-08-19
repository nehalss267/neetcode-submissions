class Solution {
    public boolean isAnagram(String s, String t) {
        //case sens
        int[] htST=new int[26];
        for(char c:s.toCharArray()){
            if(Character.isUpperCase(c)){
                htST[c-'A']++;
            }
            else
                htST[c-'a']++;
        }
        for(char c:t.toCharArray()){
            if(Character.isUpperCase(c)){
                htST[c-'A']--;
            }
            else
                htST[c-'a']--;
        }
        return Arrays.equals(htST,new int[26]);
    }
}
