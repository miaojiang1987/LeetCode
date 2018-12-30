class Solution {
public:
    vector<int> majorityElement(vector<int> &nums) {
        array<unique_ptr<int>, 2> slots;
        array<int, 2> counts;
        for(int d: nums) {
            if(slots[0] != nullptr && *slots[0] == d) {
                counts[0]++;
            }
            else if(slots[1] != nullptr && *slots[1] == d) {
                counts[1]++;
            }
            else if(slots[0] == nullptr) {
                slots[0] = make_unique<int>(d);
                counts[0] = 1;
            }
            else if(slots[1] == nullptr) {
                slots[1] = make_unique<int>(d);
                counts[1] = 1;
            }
            else {
                counts[0]--;
                counts[1]--;
            }
            if(counts[0] == 0)
                slots[0] = nullptr;
            if(counts[1] == 0)
                slots[1] = nullptr;
        }
        //cout << "counts " << counts[0] << "," << counts[1] <<endl;
        vector<int> ret;
        for(int i=0; i<2; i++) {
            if(slots[i] != nullptr) {
                int count = 0;
                for(int d: nums)
                    count += d==(*slots[i]) ? 1 : 0;
                if(count > nums.size()/3)
                    ret.push_back(*slots[i]);
            }
        }
        return ret;
    }
};
