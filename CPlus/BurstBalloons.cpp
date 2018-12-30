class Solution {
public:
    int maxCoins(vector<int> &nums) {
        nums.insert(nums.begin(), 1);
        nums.push_back(1);
        int balloons[nums.size()][nums.size()];
        for(int k=0; k<nums.size()-1; k++)
            balloons[k][k+1] = 0;
        for(int len=3; len<=nums.size(); len++) {
            for(int l=0; l+len<=nums.size(); l++) {
                int r = l + len - 1;
                balloons[l][r] = 0;
                for(int k=l+1; k<r; k++) {
                    balloons[l][r] = max(balloons[l][r], balloons[l][k]+balloons[k][r]+nums[k]*nums[l]*nums[r]);
                }
            }
        }
        return balloons[0][nums.size()-1];
    }
};