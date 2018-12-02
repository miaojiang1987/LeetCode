class Solution {
public:
    int longestSubstring(string s, int k) {
        int counts[26] = {0};
        for(char ch: s)
            counts[ch-'a']++;
        bool geq_k = true;
        for(int d: counts)
            if(d < k)
                geq_k = false;
        if(geq_k)
            return s.size();
        size_t p0 = 0, p1 = 0;
        int ret = 0;
        while(p1<s.size()) {
            while(p1<s.size() && counts[s[p1]-'a']>=k)
                p1++;
            ret = max(ret, longestSubstring(s.substr(p0, p1-p0), k));
            p0 = p1;
            while(p0<s.size() && counts[s[p0]-'a']<k)
                p0++;
        }
        return ret;
    }
};
