class NumArray {
public:
    NumArray(vector<int> nums) {
        arr.resize(nums.size());
        bitree.resize(arr.size() + 1);
        for(int i=0; i<arr.size(); i++) {
            update(i, nums[i]);
        }
       
    }
    
    void update(int i, int val) {
        int delta = val - arr[i];
        arr[i] = val;
        int index = i + 1;
        while(index <= arr.size()) {
            bitree[index] += delta;
            index += index & (-index);
        }
    }
    
    int sum(int i) {
        int ret = 0;
        i++;
        while(i > 0) {
            ret += bitree[i];
            i -= i & (-i);
        }
        return ret;
    }

    int sumRange(int i, int j) {
        return i>=0 ? sum(j)-sum(i-1) : sum(j);
    }

private:
    vector<int> arr;
    vector<int> bitree;
};


