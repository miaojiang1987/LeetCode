/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Constructor initializes an empty nested list.
 *     NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     NestedInteger(int value);
 *
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Set this NestedInteger to hold a single integer.
 *     void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     void add(const NestedInteger &ni);
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class Solution {
public:
    NestedInteger deserialize(string s) {
        int i = 0;
        if(s[i] != '[') {
            int val = nextInt(s, i);
            return NestedInteger(val);
        }
            
        
        vector<NestedInteger> st;
        while(i < s.size()) {
            if(s[i] == '[') {
                st.push_back(NestedInteger());
                i++;
            }
            else if(s[i] == ']') {
                auto last = st.back();
                st.pop_back();
                if(!st.empty())
                    st.back().add(last);
                else
                    st.push_back(last);
                i++;
            }
            else if((s[i]>='0' && s[i]<='9') || s[i]=='-') {
                st.back().add(nextInt(s, i));
            }
            else {
                i++;
            }
        }
        return st.back();
    }
    
    int nextInt(const string &s, int &pos) {
        while(pos < s.size() && (s[pos]<'0' || s[pos]>'9') && s[pos]!='-')
            pos++;
        
        int ret = 0;
        bool sign = true;
        if(s[pos] == '-') {
            //cout << "negative" << endl;
            sign = false;
            pos++;
        }
            
        while(pos < s.size() && s[pos]>='0' && s[pos]<='9') {
            ret = ret * 10 + (s[pos] - '0');
            pos++;
        }
        
        return sign ? ret : -ret;
    }
};


