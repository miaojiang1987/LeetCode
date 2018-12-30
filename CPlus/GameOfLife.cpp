class Solution {
public:
    void gameOfLife(vector<vector<int>> &board) {
        //-1: live => dead
        //-2: dead => live
        int h = board.size();
        if(h == 0)
            return;
        w = board[0].size();
        if(w == 0)
            return;
        for(int j=0; j<h; j++)
            for(int i=0; i<w; i++) {
                int lives = countLives(board, j, i);
                if(board[j][i] == 1 && (lives < 2 || lives > 3))
                    board[j][i] = -1;
                if(board[j][i] == 0 && lives == 3)
                    board[j][i] = -2;
            }
        for(int j=0; j<h; j++)
            for(int i=0; i<w; i++) {
                if(board[j][i] == -1)
                    board[j][i] = 0;
                if(board[j][i] == -2)
                    board[j][i] = 1;
            }
    }

    int countLives(vector<vector<int>> &board, int y, int x) {
        int ret = 0;
        int h = board.size(), w = board[0].size();
        if(y > 0)
            ret += board[y-1][x] ? 1 : 0;
        if(y+1 < h)
            ret += board[y+1][x] ? 1 : 0;
        if(x > 0)
            ret += board[y][x-1] ? 1 : 0;
        if(x+1 < w)
            ret += board[y][x+1] ? 1 : 0;
        
        if(y > 0 && x > 0)
            ret += board[y-1][x-1] ? 1 : 0;
        if(y+1 < h && x > 0)
            ret += board[y+1][x-1] ? 1 : 0;
        if(y > 0 && x+1 < w)
            ret += board[y-1][x+1] ? 1 : 0;
        if(y+1 < h && x+1 < w)
            ret += board[y+1][x+1] ? 1 : 0;
        
        return ret;
    }
};


