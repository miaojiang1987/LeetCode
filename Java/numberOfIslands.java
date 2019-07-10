class Solution {
    public int numIslands(char[][] grid) {
        if (grid==null || grid.length==0 || grid[0].length==0){
            return 0;
        }
        
        int row=grid.length;
        int col=grid[0].length;
        
        int result=0;
        boolean[][] visited = new boolean[row][col];
        
        for (int i=0;i<row;i++){
            for (int j=0;j<col;j++){
                if(grid[i][j]=='1' && !visited[i][j]){
                    BFS(grid,visited,i,j);
                    result++;
                }
            }
        }
        
        return result;
    }
    
    private void BFS(char[][] grid,boolean[][] visited,int x,int y){
        int[] dx={1,0,0,-1};
        int[] dy={0,1,-1,0};
        
        Queue<Integer> qx = new LinkedList<>();
        Queue<Integer> qy = new LinkedList<>();

        qx.offer(x);
        qy.offer(y);
        visited[x][y] = true;
 
         while (!qx.isEmpty()) {
            int cx = qx.poll();
            int cy = qy.poll();

            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                if (0 <= nx && nx < grid.length && 0 <= ny && ny < grid[0].length && !visited[nx][ny] && grid[nx][ny]=='1') {
                    qx.offer(nx);
                    qy.offer(ny);
                    visited[nx][ny] = true;
                }
            }
        }
        
        
    }
}