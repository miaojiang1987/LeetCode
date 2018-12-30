class Solution {
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) {
        if(s.empty() || k <= 0)
            return 0;
        long p[2] = {0, -1};
        int ret = 0;
        unordered_map<char, int> counts;
        cout << p[1] << "," << s.size()-1 << endl;
        while(p[1] < (int)s.size()-1) {
            expand(s, p, counts, k);
            //cout << "expanded:" << p[0] << "," << p[1] << endl;
            ret = max(ret, (int)(p[1] - p[0] + 1));
            //cout << "reduced:" << p[0] << "," << p[1] << endl;
            reduce(s, p, counts, k);
        }
        return ret;
    }

private:
    inline void expand(const string &s, long *p, unordered_map<char, int> &counts, int k) {
        while(p[1] < (int)s.size()-1) {
            if(counts.size() < k || (counts.size() == k && counts.find(s[p[1]+1]) != counts.end())) {
                counts[s[1+p[1]]] = counts.find(s[p[1]+1]) != counts.end() ? counts[s[1+p[1]]]+1 : 1;
                p[1]++;
            }
            else
                break;
        }
    }

    inline void reduce(const string &s, long *p, unordered_map<char, int> &counts, int k) {
        while(p[0] <= p[1] && counts.size() >= k) {
            counts[s[p[0]]]--;
            if(counts[s[p[0]]] == 0)
                counts.erase(s[p[0]]);
            p[0]++;
        }
    }
}; 
