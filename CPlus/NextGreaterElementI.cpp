#include <unordered_map>
#include <vector>


using namespace std;

class Solution {
public:
    vector<int> nextGreaterElement(vector<int> &findNums, vector<int> &nums) {
        unordered_map<int, int> next;
        vector<int> st;
        for(int i=0; i<nums.size(); i++) {
            while(!st.empty() && st.back()<=nums[i]) {
                next[st.back()] = nums[i];
                st.pop_back();
            }
            st.push_back(nums[i]);
        }
        vector<int> ret;
        for(int d: findNums) {
            if(next.find(d) == next.end())
                ret.push_back(-1);
            else
                ret.push_back(next[d]);
        }
        return ret;
    }
};
