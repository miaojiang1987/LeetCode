class Solution {
public:
    int minMoves(vector<int> &nums) {
        int low = *min_element(nums.begin(), nums.end());
        int ret = 0;
        for(int d: nums)
            ret += d - low;
        return ret;
    }
};