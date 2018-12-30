class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t ret = 0;
        uint32_t mask = 1 << 31;
        for(int i=0; i<32; i++) {
            ret += (n & 0x00000001)!=0 ? mask : 0;
            mask >>= 1;
            n >>= 1;
        }
        return ret;
    }
};
