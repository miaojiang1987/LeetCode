#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    int nextGreaterElement(int n) {
        return next(n);
    }

    int next(int n) {
        vector<char> digits;
        while(n != 0) {
            digits.push_back(n % 10);
            n /= 10;
        }
        reverse(digits.begin(), digits.end());
        size_t glitch = ~0x0UL;
        for(int i=digits.size()-2; i>=0; i--)
            if(digits[i] < digits[i+1]) {
                glitch = i;
                break;
            }
        if(glitch >= digits.size())
            return -1;
        size_t next = glitch + 1;
        for(int i=glitch+1; i<digits.size(); i++) {
            if(digits[i] > digits[glitch] && digits[i] < digits[next])
                next = i;
        }
        swap(digits[next], digits[glitch]);
        sort(digits.begin()+glitch+1, digits.end());
        int ret = 0;
        for(int d: digits) {
            if(ret * 10 / 10 != ret)
                return -1;
            ret = ret * 10 + d;
        }
        return ret;
    }
};

