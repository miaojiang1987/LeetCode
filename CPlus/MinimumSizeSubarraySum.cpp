class Solution {
public:
    int minSubArrayLen(int s, vector<int> &nums) {
        int p[2] = {0, -1};
        int cur = 0;
        int ret = -1;
        while(p[1] < (int)nums.size()) {
            expand(s, nums, p, cur);
            // cout << "expanded:" << p[0] << "," << p[1];
            // cout << " cur:" << cur << endl;
            if(cur < s)
                break;
            reduce(s, nums, p, cur);
            // cout << "reduced:" << p[0] << "," << p[1];
            // cout << " cur:" << cur << endl;
            ret = ret==-1 ? (p[1]-p[0]+1) : min(ret, p[1]-p[0]+1);
            cur -= nums[p[0]++];
            
        }
        return ret==-1 ? 0 : ret;
    }
    
    inline void expand(int s, const vector<int> &nums, int *p, int &cur) {
        while(p[1] < (int)nums.size() - 1 && cur < s) {
            cur += nums[++p[1]];
        }
    }
    
    inline void reduce(int s, const vector<int> &nums, int *p, int &cur) {
        while(p[0] <= p[1]) {
            if(cur - nums[p[0]] < s)
                break;
            cur -= nums[p[0]++];
        }
    }
};

