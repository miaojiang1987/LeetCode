using Cell = tuple<int, int, int>;


class Solution {
public:
    int trapRainWater(vector<vector<int>> &heightMap) {
        if(heightMap.empty())
            return 0;
        size_t h = heightMap.size(), w = heightMap[0].size();
        if(h <= 2 || w <= 2)
            return 0;
        priority_queue<Cell, vector<Cell>, TupleComparator> q;
        vector<vector<bool>> isVisited(h, vector<bool>(w, false));
        for(int i=0; i<w-1; i++) {
            q.emplace(0, i, heightMap[0][i]);
            isVisited[0][i] = true;
        }
        for(int i=0; i<h-1; i++) {
            q.emplace(i, w-1, heightMap[i][w-1]);
            isVisited[i][w-1] = true;
        }    
        for(int i=0; i<w-1; i++) {
            q.emplace(h-1, w-1-i, heightMap[h-1][w-1-i]);
            isVisited[h-1][w-1-i] = true;
        }
        for(int i=0; i<h-1; i++) {
            q.emplace(h-1-i, 0, heightMap[h-1-i][0]);
            isVisited[h-1-i][0] = true;
        }
        int ret = 0;
        
        while(!q.empty()) {
            auto cur = q.top();
            q.pop();
            int y = get<0>(cur), x = get<1>(cur), height = get<2>(cur);
            //cout << "y, x = " << y << " " << x << endl;
            //cout << "q size = " << q.size() << endl;
            //cout << 0 << endl;
            if(x > 0 && !isVisited[y][x-1]) {
                ret += max(0, height - heightMap[y][x-1]);
                isVisited[y][x-1] = true;
                q.emplace(y, x-1, max(height, heightMap[y][x-1]));
            }
            //cout << 1 << endl;
            if(x + 1 < w && !isVisited[y][x+1]) {
                ret += max(0, height - heightMap[y][x+1]);
                isVisited[y][x+1] = true;
                q.emplace(y, x+1, max(height, heightMap[y][x+1]));
            }
            //cout << 2 << endl;
            if(y > 0 && !isVisited[y-1][x]) {
                ret += max(0, height - heightMap[y-1][x]);
                isVisited[y-1][x] = true;
                q.emplace(y-1, x, max(height, heightMap[y-1][x]));
            }
            //cout << 3 << endl;
            if(y + 1 < h && !isVisited[y+1][x]) {
                ret += max(0, height - heightMap[y+1][x]);
                isVisited[y+1][x] = true;
                q.emplace(y+1, x, max(height, heightMap[y+1][x]));
            }
        }
        return ret;
    }
    
private:
    struct TupleComparator {
        bool operator()(const Cell &t1, const Cell &t2) const {
            return get<2>(t1) > get<2>(t2);
        }
    };
};