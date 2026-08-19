class Solution {
    public int[] topKFrequent(int[] n, int k) {
        //min heap priority queue of size k pop when size greater than k
        Map<Integer,Integer> map=new HashMap<>();
        for(int i=0;i<n.length;i++){
            map.put(n[i],map.getOrDefault(n[i],0)+1);
        }

        PriorityQueue<Integer> minHeap=new PriorityQueue<>((a,b)->map.get(a)-map.get(b));//sorted by value
        int[] ans=new int[k];
        for(int x:map.keySet()){
            minHeap.add(x);
            if(minHeap.size()>k)minHeap.poll();//size of k with keys

        }
        int i=0;
        while(!minHeap.isEmpty()){
            ans[i]=minHeap.poll();
            i++;
        }

        return ans;
    }
}
