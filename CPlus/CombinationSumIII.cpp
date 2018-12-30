class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> sol;
        vector<int> cur;
        combinationSum3(k, n, cur, sol, 0);
        return sol;
    }
    
    void combinationSum3(const int k, const int n, vector<int> &cur, vector<vector<int>> &sol, int sum) {
        //cout << sum <<"," << cur.size() << endl;
        if(cur.size() == k) {
            if(sum == n)
                sol.push_back(cur);
            return;
        }
        int next = cur.empty() ? 1 : cur.back()+1;
        for(int i=next; i<=9 && i+sum<=n; i++) {
            cur.push_back(i);
            combinationSum3(k, n, cur, sol, i+sum);
            cur.pop_back();
        }
    }
};

