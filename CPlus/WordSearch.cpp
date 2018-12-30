class Solution {
public:
    bool exist(vector<vector<char>> &board, string word) {
        if(word.empty())
            return true;
        int h = board.size();
        if(h == 0)
            return false;
        int w = board[0].size();
        if(w == 0)
            return false;
        
        vector<vector<bool>> isVisited(h, vector<bool>(w, false));
        
        for(int j=0; j<h; j++)
            for(int i=0; i<w; i++) {
                if(exist(board, word, 0, isVisited, j, i))
                    return true;
            }
        
        return false;
    }

private:
    bool exist(vector<vector<char>> &board, string &word, int index, vector<vector<bool>> &isVisited, int y, int x) {
        if(index == word.size()-1) {
            return word[index] == board[y][x];
        }
                
        if(board[y][x] != word[index])
            return false;
        
        isVisited[y][x] = true;
        bool ret = false;
        int h = board.size(), w = board[0].size();
        if(!ret && x>0 && !isVisited[y][x-1] && exist(board, word, index+1, isVisited, y, x-1)) {
            ret = true;
        }
        if(!ret && x<w-1 && !isVisited[y][x+1] && exist(board, word, index+1, isVisited, y, x+1)) {
            ret = true;
        }
        if(!ret && y>0 && !isVisited[y-1][x] && exist(board, word, index+1, isVisited, y-1, x)) {
            ret = true;
        }
        if(!ret && y<h-1 && !isVisited[y+1][x] && exist(board, word, index+1, isVisited, y+1, x)) {
            ret = true;
        }
        
        isVisited[y][x] = false;
        return ret;
    }
};


