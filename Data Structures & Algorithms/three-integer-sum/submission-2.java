class Solution {
    public List<List<Integer>> threeSum(int[] n) {
        //two pointers- 3 pointers for pointeing at triplets
        //prereq- array sorted
        //rem- handle duplicates (mentioned in q)
        //i fixed for one loop ->l,r and keep moving

        // bugs fixed-> duplicate handling
        // ensuring l<r
        // after sum=0, pointers move
        //resetting r everytime
        Arrays.sort(n);
        //-4 -1 -1 0 1 2 //sum=-3 0 0
        List<List<Integer>> ans=new ArrayList<>();
        for(int i=0;i<n.length;i++){

            if(n[i]>0)break;//positive ahead also, so no possibility of 0
            //0 considered since [0,0,0] is possible
            if(i>0 && n[i]==n[i-1]){
            //i values:
            //0 1 3 (l=1 and 0 same l++ l=2,1 same l++ l=3,2 same l++)
                continue; 
            }
            //i=0->-4 -1 2, -4 -1 2, -4 (-1 skipped due to l++) 0 2 , -4 1 2 , l==r while breaks
            //i=1-> -1 -1 2 (sum=0) (move l and r ) ,-1 0 1 (sum=0) , -1 1(l==r) while condition fails
            //i=2 continue
            //i=3 0 1 2 , r--, r=l while condition not valid anymore
            //1>0 break
            int l=i+1;
            int r=n.length-1;
            while(l<r){
                int sum=n[l]+n[r]+n[i];
                if(sum==0){
                    List<Integer>list=new ArrayList<>(Arrays.asList(n[l],n[i],n[r]));
                    ans.add(list);
                    //valid found now move both l and r
                    l++;
                    r--;
                    while(l<r && n[l]==n[l-1])l++;
                    while(l<r && n[l]==n[l-1])r--;
                }else if(sum>0)r--;
                else {
                    l++;
                }

            }
        }
        return ans;
    }
}
