class Solution {
    public void bfs(char[][] grid,int i,int j,boolean[][] v){
        int m=grid.length;
        int n=grid[0].length;
        if(i<0 || j<0 ||i>m-1||j>n-1){
            return;
        }
        if(v[i][j])return;
        if(grid[i][j]=='0')return;
        v[i][j]=true;
        bfs(grid,i-1,j,v);
        bfs(grid,i,j-1,v);
        bfs(grid,i+1,j,v);
        bfs(grid,i,j+1,v);
    }
    public int numIslands(char[][] grid) {
        //bfs
        int m=grid.length;
        int n=grid[0].length;
        boolean[][] v=new boolean[m][n];
        int ans=0;

        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                //valid only if its 1
                if(!v[i][j] && grid[i][j]=='1'){
                    bfs(grid,i,j,v);
                    ans++;
                }
            }
        }
        return ans;
    }
}
