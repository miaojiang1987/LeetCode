#include <functional>

class Solution {
public:
    void wiggleSort(vector<int> &nums) {
        if(nums.size() <= 1)
            return;
        vector<function<bool(int, int)>> compare;
        compare.push_back(
            [](int a, int b) {
                return a <= b;
            }
        );
        compare.push_back(
            [](int a, int b) {
                return a >= b;
            }
        );
        for(int i=0; i<nums.size()-1; i++) {
            if(!compare[i%2](nums[i], nums[i+1]))
                swap(nums[i], nums[i+1]);
        }
    }
};
