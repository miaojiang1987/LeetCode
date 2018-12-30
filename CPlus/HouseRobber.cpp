class Solution {
public:
    int rob(vector<int> &nums) {
        if(nums.empty())
            return 0;
        int ret = 0;
        int onProfits[nums.size()];
        int offProfits[nums.size()];
        
        onProfits[0] = nums[0];
        offProfits[0] = 0;
        for(int i=1; i<nums.size(); i++) {
            onProfits[i] = offProfits[i-1] + nums[i];
            offProfits[i] = max(offProfits[i-1], onProfits[i-1]);
        }
        return max(onProfits[nums.size()-1], offProfits[nums.size()-1]);
    }
};