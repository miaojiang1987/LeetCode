class Codec {
public:

    // Encodes a list of strings to a single string.
    string encode(const vector<string> &strs) {
        string ret;
        auto escape = [](const string &s) {
            string escaped;
            for(size_t i=0; i<s.size(); i++) {
                escaped.push_back(s[i]);
                if(s[i] == '\"') {
                    escaped.push_back(s[i]);
                }
            }
            return escaped;
        };
        for(const string &s: strs) {
            if(!ret.empty())
                ret.push_back('\n');
            ret.append("\"" + escape(s) + "\"");
        }
        //cout << "encoded = " << ret << endl;
        return ret;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> ret;
        auto unescape = [](const string &s) {
            string unescape;
            for(size_t i=0; i<s.size(); i++) {
                unescape.push_back(s[i]);
                if(i<s.size()-1 && s[i+1] == '\"') {
                    i++;
                }
            }
            return unescape;
        };
        int p0 = 0, p1 = 0;
        while(p0 < s.size()) {
            p1 = p0 + 1;
            while(p1<s.size()
                  && !(p1<s.size()-1 && s[p1]=='\"' && s[p1+1]=='\n')
                  && !(s[p1]=='\"' && p1==s.size()-1)) {
                p1++;
            }
            //cout << "sub=" << s.substr(p0, p1-p0) << endl;
            ret.push_back(unescape(s.substr(p0+1, p1-p0-1)));
            p0 = p1 + 2;
        }
        //cout << "size=" << ret.size() << endl;
        return ret;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));

