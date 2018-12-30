class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> counts;
        for(char ch: s) {
            if(counts.find(ch) == counts.end())
                counts[ch] = 0;
            counts[ch]++;
        }
        vector<pair<char, int>> wordcounts;
        for(auto it=counts.begin(); it!=counts.end(); it++) {
            wordcounts.emplace_back(it->first, it->second);
        }
        sort(wordcounts.begin(), wordcounts.end(), [](const pair<char, int> &p1,
                                                      const pair<char, int> &p2) {
            return p1.second > p2.second;
        });
        string ret;
        for(auto &p: wordcounts)
            ret.append(string(p.second, p.first));
        return ret;
    }
};

