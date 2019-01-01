class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int left=-1;
        int longest=0;
        unordered_map<int,int> map;
        
        for(int i=0;i<s.size();i++){
            if(map.count(s[i]) && map[s[i]] > left){
                left=map[s[i]];
            }
            map[s[i]]=i;
            longest=max(longest,i-left);            
        }
        return longest;
    }
};