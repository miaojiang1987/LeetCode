class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n1 = s1.size(), n2 = s2.size(), left = 0,count=n1;
        vector<int> m(128);
        for (char c : s1) ++m[c];
        for(int i=0;i<n2;i++){
            if(m[s2[i]]-->0) count--;
            while(count==0){
                if (i - left + 1 == n1) return true;
                if (++m[s2[left++]] > 0) ++count;
            }
        }
        return false;
    }
};