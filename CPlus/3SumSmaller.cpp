class Solution {
public:
    int threeSumSmaller(vector<int> &nums, int target) {
        sort(nums.begin(), nums.end());
        int ret = 0;
        for(int i=0; i<(int)nums.size()-2; i++) {
            int start = i + 1;
            int end = nums.size() - 1;
            while(start < end) {
                int sum = nums[i] + nums[start] + nums[end];
                if(sum < target) {
                    ret += end - start;
                    start++;
                }
                else {
                    end--;
                }
            }
        }
        return ret;
    }
};

