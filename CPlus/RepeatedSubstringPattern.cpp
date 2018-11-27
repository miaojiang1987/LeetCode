#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        if(s.empty())
            return true;
        for(size_t len=1; len<s.size(); len++) {
            if(s.size() % len != 0)
                continue;
            if(IsRepeated(s, len))
                return true;
        }
        return false;
    }

    bool IsRepeated(const string &s, size_t len) {
        for(int i=0; i<s.size(); i+=len) {
            if(s.substr(i, len) != s.substr(0, len))
                return false;
        }
        return true;
    }
};

