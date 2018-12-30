class Solution {
public:
    int maxKilledEnemies(vector<vector<char>> &grid) {
        if(grid.empty() || grid[0].empty())
            return 0;
        size_t h = grid.size(), w = grid[0].size();
        vector<vector<int>> rowScore(h, vector<int>(w));
        vector<vector<int>> colScore(h, vector<int>(w));
        
        for(int k=0; k<h; k++)
            scanRow(grid, rowScore, k);
        for(int k=0; k<w; k++)
            scanCol(grid, colScore, k);
        
        int ret = 0;
        for(int j=0; j<h; j++)
            for(int i=0; i<w; i++) {
                if(grid[j][i] == '0')
                    ret = max(ret, rowScore[j][i] + colScore[j][i]);
            }
        return ret;
    }

private:
    inline void scanRow(vector<vector<char>> &grid, vector<vector<int>> &rowScore, int row) {
        int cur = 0;
        vector<int> positions;
        for(int k=0; k<grid[0].size(); k++) {
            if(grid[row][k] == 'E') {
                cur++;
            }
            else if(grid[row][k] == 'W') {
                for(int p: positions)
                    rowScore[row][p] = cur;
                positions.clear();
                cur = 0;
            }
            else {
                positions.push_back(k);
            }
        }
        if(!positions.empty())
            for(int p: positions)
                rowScore[row][p] = cur;
    }
    
    inline void scanCol(vector<vector<char>> &grid, vector<vector<int>> &colScore, int col) {
        int cur = 0;
        vector<int> positions;
        for(int k=0; k<grid.size(); k++) {
            if(grid[k][col] == 'E') {
                cur++;
            }
            else if(grid[k][col] == 'W') {
                for(int p: positions)
                    colScore[p][col] = cur;
                positions.clear();
                cur = 0;
            }
            else {
                positions.push_back(k);
            }
        }
        if(!positions.empty())
            for(int p: positions)
                colScore[p][col] = cur;
    }
};

