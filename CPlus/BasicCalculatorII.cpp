class Solution {
public:
    int calculate(string s) {
        vector<char> st;
        vector<string> tokens;
        int index = 0;
        while(index < s.size()) {
            string next = Solution::nextToken(s, index);
            if(next.empty())
                break;
            if(Solution::operators.find(next[0]) != Solution::operators.end()) {
                if(st.empty() || st.back() == '(')
                    st.push_back(next[0]);
                else {
                    while(!st.empty() && st.back()!='(' && !isPreemptive(next[0], st.back())) {
                        tokens.push_back(string(1, st.back()));
                        st.pop_back();
                    }
                    st.push_back(next[0]);
                }
            }
            else if(next[0] == '(') {
                st.push_back(next[0]);
            }
            else if(next[0] == ')') {
                while(st.back()!='(') {
                    tokens.push_back(string(1, st.back()));
                    st.pop_back();
                }
                st.pop_back();
            }
            else {
                tokens.push_back(next);
            }
        }

        while(!st.empty()) {
            tokens.push_back(string(1, st.back()));
            st.pop_back();
        }
//        for(auto t: tokens)
//            cout << t << " ";
        return evalRPN(tokens);
    }

    int evalRPN(vector<string> &tokens) {
        vector<int> st;
        for(string &token: tokens) {
            if((token[0]>='0' && token[0]<='9') ||
               (token[0]=='-' && token.size()>1)) {
                st.push_back(stoi(token));
            }
            else {
                int b = st.back();
                st.pop_back();
                int a = st.back();
                st.pop_back();
                st.push_back(Solution::operators[token[0]](a, b));
            }
        }
        return st.back();
    }

private:
    static map<char, int(*)(int,int)> operators;
    static string nextToken(const string &s, int &start) {
        if(start >= s.size())
            return string();
        while(isspace(s[start]))
            start++;
        string ret;
        if(s[start] == '(' ||
        s[start] == ')' ||
        Solution::operators.find(s[start]) != Solution::operators.end()) {
            ret = string(1, s[start++]);
        }
        else {
            while(s[start]>='0' && s[start]<='9')
                ret.push_back(s[start++]);
        }
        return ret;
    }

    inline bool isPreemptive(char a, char b) {
        return (a=='*' || a=='/') && (b=='+' || b=='-');
    }
};

map<char, int(*)(int,int)> Solution::operators {
    {'+', [](int a, int b) {return a + b;}},
    {'-', [](int a, int b) {return a - b;}},
    {'*', [](int a, int b) {return a * b;}},
    {'/', [](int a, int b) {return a / b;}}
};


