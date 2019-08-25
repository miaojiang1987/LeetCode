class Solution {
public:
    int longestArithSeqLength(vector<int>& A) {
        unordered_map<int,unordered_map<int,int>> dp;
        if (A.size() <= 1) {
            return A.size();
        }
        int result=2;
        for (int i=0;i<A.size();i++){
            for (int j=0;j<i;j++){
                int diff=A[i]-A[j];
                if(!dp[diff].count(i)){
                    dp[diff][i]=2;
                }
                
                dp[diff][i]=max(dp[diff][j]+1,dp[diff][i]);
                result=max(result,dp[diff][i]);    
                
            }
        }
        return result;
    }
};