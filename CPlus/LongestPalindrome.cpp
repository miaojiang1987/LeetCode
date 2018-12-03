class Solution {
public:
    int longestPalindrome(string s) {
        int cmap[256] = {0};
        for(char c: s)
            cmap[c]++;
        int ret = 0;
        bool oddsize = false;
        for(int d: cmap) {
            if(d > 0) {
                ret += d%2==0 ? d : d-1;
            }
            if(d%2 > 0)
                oddsize = true;
        }
            
        return oddsize ? (ret+1) : ret;
    }           
};

