class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        int combos[target + 1];
        combos[0] = 1;
        for(int cur=1; cur<=target; cur++) {
            combos[cur] = 0;
            for(int d: nums) {
                if(cur - d >= 0) {
                    combos[cur] += combos[cur - d];
                }
            }
        }
        return combos[target];
    }
};