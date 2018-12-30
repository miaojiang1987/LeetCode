class Solution {
public:
    int coinChange(vector<int> &coins, int amount) {
        int counts[amount + 1] = {0};
        for(int cur=1; cur<=amount; cur++) {
            counts[cur] = -1;
            for(int d: coins) {
                if(cur - d >= 0) {
                    if(counts[cur-d]>=0 && (counts[cur]==-1 || counts[cur]>counts[cur-d]+1))
                        counts[cur] = counts[cur-d] + 1;
                }
            }
        }
        return counts[amount];
    }
};