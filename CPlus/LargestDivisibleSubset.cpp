class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int> &nums) {
        if(nums.empty())
            return vector<int>();
        vector<vector<int>> sets(nums.size());
        sort(nums.begin(), nums.end());
        int i = -1;
        for(int k=0; k<nums.size(); k++) {
            int next = -1;
            for(int j=k-1; j>=0; j--) {
                if(nums[k] % nums[j] == 0 && (next < 0 || sets[j].size() > sets[next].size()))
                    next = j;
            }
            //cout << "next=" << next << endl;
            if(next >= 0)
                sets[k].insert(sets[k].begin(), sets[next].begin(), sets[next].end());
            sets[k].push_back(nums[k]);
            //cout << "cur size = " << sets[k].size() << endl;
            if(i < 0 || sets[i].size() < sets[k].size())
                i = k;
        }
        return sets[i];
    }
};
