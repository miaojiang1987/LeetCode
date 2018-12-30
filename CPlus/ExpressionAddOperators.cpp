class Solution {
public:
    vector<string> addOperators(string num, int target) {
        string cur;
        vector<string> sol;
        addOperators(num, target, 0, cur, sol, 0, 0);
        return sol;
    }

private:
    void addOperators(const string &num, int target, int index, string &cur, 
                      vector<string> &sol, long long val, long long delta) {
        if(index >= num.size()) {
            if(val == target)
                sol.push_back(cur);
            return;
        }
        
        size_t curlen = cur.size();
        if(cur.empty()) {
            for(int i=index; i<num.size(); i++) {
                string nextnum = num.substr(index, i-index+1);
                long long nextval = stoll(nextnum);
                cur.append(nextnum);
                addOperators(num, target, i+1, cur, sol, nextval, nextval);
                cur.resize(curlen);
                if(num[index] == '0')
                    break;
            }
            return;
        }
        
        for(int i=index; i<num.size(); i++) {
            string nextnum = num.substr(index, i-index+1);
            long long nextval = stoll(nextnum);

            cur.append("+" + nextnum);
            addOperators(num, target, i+1, cur, sol, val + nextval, nextval);
            cur.resize(curlen);

            cur.append("-" + nextnum);
            addOperators(num, target, i+1, cur, sol, val - nextval, -nextval);
            cur.resize(curlen);

            cur.append("*" + nextnum);
            addOperators(num, target, i+1, cur, sol, val-delta + delta*nextval, delta*nextval);
            cur.resize(curlen);

            if(num[index] == '0')
                break;
        }
    }
};

