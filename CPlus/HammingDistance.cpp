#include <bitset>

class Solution {
public:
    int hammingDistance(int x, int y) {
        bitset<32> mask = bitset<32>(x) ^ bitset<32>(y);
        return mask.count();
    }
};