class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> ans=new ArrayList<>();
        Map<String,List<String>> map=new HashMap<>();
        for(String s:strs){
            char[] a=s.toCharArray();
            int[] ht=new int[26];//hashtable
            for(char c: a){
                ht[c-'a']++;
            }
            String htS=Arrays.toString(ht);
            map.putIfAbsent(htS,new ArrayList<>());
            map.get(htS).add(s);
        }
        // for(Map.Entry<String,List<String>> e:map.entrySet()){
        //     ans.add(e.getValue());
        // }
        ans.addAll(map.values());
        return ans;
    }
}
