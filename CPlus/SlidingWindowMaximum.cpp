class Solution {
public:
    vector<int> maxSlidingWindow(vector<int> &nums, int k) {
        vector<int> ret;
        if(nums.empty())
            return ret;
        deque<int> q;
        for(int i=0; i<k; i++) {
            while(!q.empty() && nums[q.back()]<nums[i])
                q.pop_back();
            q.push_back(i);
            while(i - q.front() + 1 > k)
                q.pop_front();
        }
        
        ret.push_back(nums[q.front()]);
        //cout << "qsize=" << q.size() << endl;
        for(int i=k; i<nums.size(); i++) {
            //cout << "i=" << i << endl;
            while(!q.empty() && nums[q.back()]<nums[i])
                q.pop_back();
            q.push_back(i);
            while(i - q.front() + 1 > k) {
                //cout << "front=" << q.front() << endl;
                q.pop_front();
                //cout << "qsize=" << q.size() << endl;
            }
            ret.push_back(nums[q.front()]);
        }
        return ret;
    }
};

