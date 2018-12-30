class Solution {
public:
    int maximalSquare(vector<vector<char>> &matrix) {
        size_t h = matrix.size();
        if(h == 0)
            return 0;
        size_t w = matrix[0].size();
        if(w == 0)
            return 0;
        
        int ret = 0;
        int sq[h][w];
        for(int k=0; k<w; k++) {
            sq[0][k] = matrix[0][k]=='1' ? 1 : 0;
            if(sq[0][k] > 0)
                ret = 1;
        }
            
        
        for(int k=0; k<h; k++) {
            sq[k][0] = matrix[k][0]=='1' ? 1 : 0;
            if(sq[k][0] > 0)
                ret = 1;
        }
        
            
        for(int j=1; j<h; j++)
            for(int i=1; i<w; i++) {
                sq[j][i] = matrix[j][i]=='1' ? 1 : 0;
                if(sq[j][i] == 0)
                    continue;
                int next = min(sq[j][i-1], sq[j-1][i]);
                next = min(next, sq[j-1][i-1]);
                sq[j][i] = next + 1;
                ret = max(sq[j][i], ret);
            }

        return ret * ret;
    }
};
