/*
Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        //dfs -> clone neighbours
        //connect each node with new Node
        Map<Node,Node> oldToNew=new HashMap<>();
        return dfs(node,oldToNew);
    }
    public Node dfs(Node node,Map<Node,Node> oldToNew){
        if(node==null)return null;
        if(oldToNew.containsKey(node))return oldToNew.get(node);
        //o(v)
        Node newN=new Node(node.val);
        oldToNew.put(node,newN);
        //o(E)
        for(Node n:node.neighbors){
            //add nei for new node
            newN.neighbors.add(dfs(n,oldToNew));//add what dfs returns 
        }
        return newN;
        //o(v)+o(e)=o(v+e)
// Time: O(V + E) because every vertex is processed once and every edge is examined during neighbor traversal.

// Auxiliary space: O(V) because the hashmap/visited structure stores each vertex once and DFS recursion can go as deep as V.

    }
}