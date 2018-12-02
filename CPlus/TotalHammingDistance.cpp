#include <bitset>
#include <vector>


class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        vector<int> ones(32);
        for(int d: nums) {
            unsigned int mask = 0x80000000;
            for(int i=0; i<32; i++) {
                if((mask & d) != 0) {
                    ones[i]++;
                }
                mask >>= 1;
            }
        }
        int ret = 0;
        for(int d: ones) {
            ret += d * (nums.size()-d);
        }
        return ret;
    }
};
