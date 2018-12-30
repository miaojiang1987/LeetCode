class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.empty())
            return 0;
        if(nums.size() == 1)
            return nums[0];
        return max(robLinear(nums, 0, nums.size()-1), robLinear(nums, 1, nums.size()-1));
    }
    
    int robLinear(vector<int> &nums, int start, int size) {
        if(size <= 0)
            return 0;

        int onProfits[size];
        int offProfits[size];
        
        onProfits[0] = nums[start];
        offProfits[0] = 0;
        for(int i=1; i<size; i++) {
            onProfits[i] = offProfits[i-1] + nums[i+start];
            offProfits[i] = max(offProfits[i-1], onProfits[i-1]);
        }
        return max(onProfits[size-1], offProfits[size-1]);
    }
};
