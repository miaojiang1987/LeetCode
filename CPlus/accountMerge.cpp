class Solution {
public:
    int find(int x) {
        if (x == father[x])
            return x;
        return father[x] = find(father[x]);
    }
    
    void connect(int a, int b) {
        int root_a = find(a);
        int root_b = find(b);
        if (root_a != root_b) {
            father[root_b] = root_a;
        }
    }
    
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        int n = accounts.size();
        father.resize(n);
        for (int i = 0; i < n; ++i)
            father[i] = i;
        
        // 以每个email作为key去union accounts indexes
        unordered_map<string, int> hash;
        for (int i = 0; i < n; ++i) {
            for (int j = 1; j < accounts[i].size(); ++j) {
                if (hash.count(accounts[i][j])) {
                    int k = hash[accounts[i][j]];
                    if (accounts[k][0] == accounts[i][0]) connect(i, k);
                } else {
                    hash[accounts[i][j]] = i;
                }
            }
        }
        
        // 以union过的accounts ids来构造合并后的accounts，并保持string order
        map<int, set<string>> merged;
        for (int i = 0; i < n; ++i) {
            int k = find(i);
            merged[k].insert(accounts[i].begin(), accounts[i].end());
        }
        
        // 构造最终答案 vector<vector<string>>
        vector<vector<string>> res;
        for (auto i : merged)
            res.push_back(vector<string>(i.second.begin(), i.second.end()));
        
        return res;
    }
private:
    vector<int> father;
};
