class Solution {
    public int orangesRotting(int[][] grid) {
        if(grid == null || grid.length == 0) return 0;
        int rows = grid.length;
        int cols = grid[0].length;
        Queue<int[]> queue = new LinkedList<>();
        int fresh = 0;
        for(int i=0; i<rows; i++){
            for(int j=0; j<cols; j++){
                if(grid[i][j] == 2) queue.offer(new int[]{i, j});
                else if(grid[i][j] == 1) fresh++;
            }
        }
        
        if(fresh == 0) return 0;
        int minutes = 0, count = 0;
        int dx[] = {0, 0, 1, -1};
        int dy[] = {1, -1, 0, 0};
        
        while(!queue.isEmpty()){
            int size = queue.size();
            for(int i=0; i<size; i++){
                int[] point = queue.poll();
                for(int j=0; j<4; j++){
                    int x = point[0] + dx[j];
                    int y = point[1] + dy[j];
                    if(x<0 || x>=rows || y<0 || y>=cols) continue;
                    if(grid[x][y] == 1){
                        grid[x][y] = 2;
                        queue.offer(new int[]{x, y});
                        count++;
                    }
                }
            }
            if(!queue.isEmpty()) minutes++;
        }
        
        return fresh == count ? minutes : -1;
    }
}