class Solution {
public:
    int lengthLongestPath(string input) {
        vector<string> tokens = split(input, '\n');
        
        vector<int> st;
        int cur = 0;
        bool isfile = false;
        size_t ret = 0;
        for(string &t: tokens) {
            int tabcount = tabs(t);
            if(tabcount <= (int)st.size() - 1)
                if(isfile)
                    ret = max(ret, cur + st.size() - 1);
            while(tabcount <= (int)st.size() - 1) {
                isfile = false;
                cur -= st.back();
                st.pop_back();
            }
            st.push_back(t.size() - tabcount);
            if(t.find('.') != string::npos)
                isfile = true;
            cur += st.back();
        }
        if(isfile)
            ret = max(ret, cur + st.size() - 1);
        return ret;
    }
    
    vector<string> split(const std::string &text, char sep) {
        vector<string> tokens;
        size_t start = 0, end = 0;
        while ((end = text.find(sep, start)) != std::string::npos) {
            tokens.push_back(text.substr(start, end - start));
            start = end + 1;
        }
        tokens.push_back(text.substr(start));
        return tokens;
    }
    
    size_t tabs(const string &t) {
        size_t ret = 0;
        while(t[ret] == '\t')
            ret++;
        return ret;
    }
    
    
};
