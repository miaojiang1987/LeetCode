class Solution {
public:
    int minCut(string s) {
        bool pmap[s.size()][s.size()];
        for(int k=0; k<s.size(); k++)
            pmap[k][k] = true;
        int cuts[s.size()+1];
        fill(cuts, cuts+s.size()+1, s.size());
        cuts[0] = 0;
        for(int i=1; i<s.size(); i++) 
            for(int j=i-1; j>=0; j--) {
                if(j + 1 == i)
                    pmap[j][i] = s[j]==s[i];
                else
                    pmap[j][i] = s[j]==s[i] && pmap[j+1][i-1];
            }
        //cout << "pmap=" << pmap[0][0] << endl;
        for(int i=0; i<s.size(); i++) {
            if(pmap[0][i]) {
                cuts[i+1] = 0;
                continue;
            }
            for(int j=i; j>0; j--) {
                if(pmap[j][i]) {
                    cuts[i+1] = min(cuts[i+1], cuts[j] + 1); 
                }
            }
        }
            
        return cuts[s.size()];
    }
};


