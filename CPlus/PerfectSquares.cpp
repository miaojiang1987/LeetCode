class Solution {
public:
    int numSquares(int n) {
        int sq[n + 1];
        sq[0] = 0;
        sq[1] = 1;
        for(int k=2; k<=n; k++) {
            sq[k] = n;
            int cur = 1;
            while(cur * cur <= k) {
                sq[k] = min(sq[k], sq[k - cur * cur] + 1);
                cur++;
            }
                
        }
        return sq[n];
    }
};
