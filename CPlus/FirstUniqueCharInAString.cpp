class Solution {
public:
    int firstUniqChar(string s) {
        int cmap[26] = {0};
        for(char ch: s)
            cmap[ch-'a']++;
        for(int i=0; i<s.size(); i++)
            if(cmap[s[i]-'a']==1)
                return i;
        return -1;
    }
};