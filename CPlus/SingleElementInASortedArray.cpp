#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    int singleNonDuplicate(vector<int> &nums) {
        //001100110
        //001110011
        size_t start = 0, end = nums.size() - 1;
        while(start <= end) {
            if(end == start)
                return nums[end];
            size_t mid = start + (end-start)/2;
            if(mid%2 == 0) {
                if(nums[mid+1] == nums[mid])
                    start = mid + 2;
                else
                    end = mid;
            }
            else {
                if(nums[mid-1] == nums[mid])
                    start = mid + 1;
                else
                    end = mid;
            }
        }
        return 0;
    }
};