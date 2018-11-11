class Solution {
public:
    string reverseString(string s) {
        int left=0;
        int right=s.size()-1;
        while(left<right){
            char t=s[left];
            s[left++]=s[right];
            s[right--]=t;
        }
        return s;
    }
};