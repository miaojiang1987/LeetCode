#include <unordered_map>

class Solution {
public:
    int fourSumCount(vector<int> &A, vector<int> &B, vector<int> &C, vector<int> &D) {
        unordered_map<int, int> sums;
        size_t n = C.size();
        for(int i=0; i<n; i++)
            for(int j=0; j<n; j++) {
                if(sums.find(C[i] + D[j]) == sums.end())
                    sums[C[i] + D[j]] = 0;
                sums[C[i] + D[j]]++;
            }
        int ret = 0;
        for(int i=0; i<n; i++)
            for(int j=0; j<n; j++) {
                if(sums.find(-A[i]-B[j]) != sums.end())
                    ret += sums[-A[i]-B[j]];
            }
        return ret;
    }
};
