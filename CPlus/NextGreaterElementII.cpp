#include <unordered_map>
#include <vector>


using namespace std;

class Solution {
public:
    vector<int> nextGreaterElements(vector<int> &nums) {
        unordered_map<int, int> next;
        vector<int> st;
        for(int i=0; i<nums.size()*2; i++) {
            while(!st.empty() && nums[st.back()]<nums[i%nums.size()]) {
                next[st.back()] = nums[i%nums.size()];
                st.pop_back();
            }
            st.push_back(i%nums.size());
        }
        vector<int> ret;
        for(int i=0; i<nums.size(); i++) {
            if(next.find(i) == next.end())
                ret.push_back(-1);
            else
                ret.push_back(next[i]);
        }
        return ret;
    }
};