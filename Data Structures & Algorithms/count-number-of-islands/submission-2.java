class Solution {
    public void dfs(char[][] grid,int i,int j,boolean[][] v){
        int m=grid.length;
        int n=grid[0].length;
        if(i<0 || j<0 ||i>m-1||j>n-1){
            return;
        }
        if(v[i][j])return;
        if(grid[i][j]=='0')return;
        v[i][j]=true;
        dfs(grid,i-1,j,v);
        dfs(grid,i,j-1,v);
        dfs(grid,i+1,j,v);
        dfs(grid,i,j+1,v);
    }
    public int numIslands(char[][] grid) {
        //dfs
        int m=grid.length;
        int n=grid[0].length;
        boolean[][] v=new boolean[m][n];
        int ans=0;

        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                //valid only if its 1
                if(!v[i][j] && grid[i][j]=='1'){
                    dfs(grid,i,j,v);
                    ans++;
                }
            }
        }
        return ans;
    }
}
