class Solution {
    //multi source bfs
    //simultaneously from all sources
    // grid[r][c] != Integer.MAX_VALUE for visited
    // Then BFS expands simultaneously from all of them.
    //mental model 
//     q=()
//     for(i){
//         for(j){
//             if(source){
//                 q.add(source)
//             }
//         }
//     }
//     if(q empty)return 0
//     int[] dir
//     // 1. Add ALL sources
// for (...) {
//     if (isSource)
//         q.add(source);
// }

// // 2. BFS normally
// while (!q.isEmpty()) {

//     current = q.poll();

//     for (neighbor : neighbors) {

//         if (unvisited) {

//             neighbor.distance =
//                 current.distance + 1;

//             q.add(neighbor);
//         }
//     }
// }
//     // while(q not empty){
//     //     coordinates=q.poll
//     //     x=cord[0]
//     //     y=cord[1]
//     //     for(d[]:dir){
//     //         r=d[0]+x
//     //         c=d[1]+y
//     //         if(not valid r/c)continue
//     //         if(visited)continue
//     //         if(invalid cell)continue
//     //         q.add([r,c])//visited added in q
//     //         grid[x][y]=grid[r][c]+1
//     //     }
//     // } 
    
    public void islandsAndTreasure(int[][] grid) {
        int m=grid.length;
        int n=grid[0].length;
        Queue<int[]> q=new LinkedList<>();
        //find source
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]==0)
                    q.add(new int[]{i,j});
            }
        }
        if(q.size()==0)return;
        int[][] dir={{0,1},{1,0},{-1,0},{0,-1}};
        //bfs
        while(!q.isEmpty()){
            int[] coordinates=q.poll();
            int row=coordinates[0];
            int col=coordinates[1];
            for(int dr[]:dir){
                    int r=dr[0]+row;
                    int c=dr[1]+col;
                    if(r<0||c<0||r>m-1||c>n-1||grid[r][c]!=Integer.MAX_VALUE)continue;//go to start of loop
                    
                    grid[r][c]=grid[row][col]+1;
                    //add to q since visited
                    q.add(new int[]{r,c});
                
            }
        }
    }
}
