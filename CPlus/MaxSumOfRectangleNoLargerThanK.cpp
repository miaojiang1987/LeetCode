class Solution {
public:
    int maxSumSubmatrix(vector<vector<int>> &matrix, int k) {
        int ret = INT_MIN;
        int h = matrix.size(), w = matrix[0].size();
        for(int row0=0; row0<h; row0++) {
            vector<int> heights(w);
            for(int row1=row0; row1<h; row1++) {
                for(int k=0; k<w; k++)
                    heights[k] += matrix[row1][k];
                ret = max(ret, largestSubarrayLeqK(heights, k));
            }
        }
        return ret;
    }

    int largestSubarrayLeqK(const vector<int> &arr, int k) {
        set<int> sums;
        sums.insert(0);
        int cur = 0;
        int ret = INT_MIN;

        for(int d: arr) {
            cur += d;
            auto it = sums.lower_bound(cur - k);
            if(it != sums.end())
                ret = max(ret, cur - *it);
            sums.insert(cur);
        }
        
        return ret;
    }
};


