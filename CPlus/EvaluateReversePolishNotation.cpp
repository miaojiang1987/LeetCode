class Solution {
public:
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
};

map<char, int(*)(int,int)> Solution::operators {
        {'+', [](int a, int b) {return a + b;}},
        {'-', [](int a, int b) {return a - b;}},
        {'*', [](int a, int b) {return a * b;}},
        {'/', [](int a, int b) {return a / b;}}
};
