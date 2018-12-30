class Solution {
public:
    int maxSubArrayLen(vector<int> &nums, int k) {
        unordered_map<int, int> sums;
        int sum = 0;
        for(int i=0; i<nums.size(); i++) {
            sum += nums[i];
            if(sums.find(sum) == sums.end())
                sums[sum] = i;
        }
        int ret = 0;
        sum = 0;
        for(int i=0; i<nums.size(); i++) { 
            sum += nums[i];
            if(sums.find(sum - k) != sums.end())
                ret = max(ret, i - sums[sum-k]);
            if(sum == k)
                ret = max(ret, i+1);
        }
        return ret;
    }
};

