class Solution {
public:
    int lengthOfLIS(vector<int> &nums) {
        vector<int> endings;
        for(int d: nums) {
            size_t pos = searchInsert(endings, d);
            if(pos >= endings.size())
                endings.push_back(d);
            endings[pos] = d;
        }
        return endings.size();
    }

    int searchInsert(const vector<int> &nums, int target) {
        if(nums.empty())
            return 0;
        size_t start = 0, end = nums.size() - 1;
        if(target > nums[end])
            return end + 1;
        while(start <= end) {
            if(end == start)
                return end;
            if(end == start + 1) {
                if(target <= nums[start])
                    return start;
                if(target <= nums[end])
                    return end;
                return end + 1;
            }
            size_t mid = start + (end-start) / 2;
            if(target <= nums[mid])
                end = mid;
            else
                start = mid;
        }
        return -1;
    }
};
