class Solution {
public:
    vector<string> summaryRanges(vector<int> &nums) {
        int p0 = 0, p1 = 1;
        vector<string> ret;
        while(p1 < nums.size()) {
            if((long)nums[p1] - (long)nums[p1-1] > 1) {
                ret.push_back(p1-1==p0 ? to_string(nums[p0]) : to_string(nums[p0])+"->"+to_string(nums[p1-1]));
                p0 = p1;
            }
            p1++;
        }
        if(p0 < nums.size()) 
            ret.push_back(p1-1==p0 ? to_string(nums[p0]) : to_string(nums[p0])+"->"+to_string(nums[p1-1]));
        return ret;
    }
};