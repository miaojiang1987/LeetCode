class Solution {
public:
    vector<pair<int, int>> getSkyline(vector<vector<int>> &buildings) {
        unordered_map<int, pair<vector<int>, vector<int>>> pts;
        for(auto &build: buildings) {
            pts[build[0]].first.push_back(build[2]);
            pts[build[1]].second.push_back(build[2]);
        }
        
        vector<int> ptlist;
        for(auto it=pts.begin(); it!=pts.end(); it++)
            ptlist.push_back(it->first);
        sort(ptlist.begin(), ptlist.end());
        
        vector<pair<int, int>> ret;
        map<int, int> heights;
        int cur = -1;
        for(int pt: ptlist) {
            //cout << pt << endl;
            for(int d: pts[pt].first) {
                if(heights.find(d) == heights.end())
                    heights[d] = 0;
                heights[d]++;
            }
            for(int d: pts[pt].second) {
                heights[d]--;
                if(heights[d] == 0)
                    heights.erase(d);
            }

            int next = heights.empty() ? 0 : heights.rbegin()->first;
            if(cur != next) {
                cur = next;
                ret.emplace_back(pt, cur);
            }
        }
        return ret;
    }
};