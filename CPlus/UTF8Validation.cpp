class Solution {
public:
    bool validUtf8(vector<int> &data) {
        size_t index = 0;
        while(index < data.size()) {
            if(!validUtf8(data, index))
                return false;
        }
        return true;
    }
    
    bool validUtf8(vector<int> &data, size_t &index) {
        if((data[index] & 0x80) == 0) {
            index++;
            return true;
        }
        if((0xE0 & ~(data[index] ^ 0xC0)) == 0xE0) {
            index++;
            return (0xC0 & ~(data[index++] ^ 0x80)) == 0xC0;
        }
        if((0xF0 & ~(data[index] ^ 0xE0)) == 0xF0) {
            index++;
            return (0xC0 & ~(data[index++] ^ 0x80)) == 0xC0
                && (0xC0 & ~(data[index++] ^ 0x80)) == 0xC0;
        }
        if((0xF8 & ~(data[index] ^ 0xF0)) == 0xF8) {
            index++;
            return (0xC0 & ~(data[index++] ^ 0x80)) == 0xC0
                && (0xC0 & ~(data[index++] ^ 0x80)) == 0xC0
                && (0xC0 & ~(data[index++] ^ 0x80)) == 0xC0;
        }
        return false;
    }
};
