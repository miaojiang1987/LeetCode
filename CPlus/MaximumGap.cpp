namespace sorting {
    size_t partition(vector<int> &nums, size_t start, size_t end) {
        if(start >= end)
            return end;
        if(start == end - 1) {
            if(nums[start] > nums[end])
                swap(nums[start], nums[end]);
            return end;
        }
        //cout << "start=" << start << " end=" << end << endl;
        size_t mid = start + (end-start) / 2;
        swap(nums[start], nums[mid]);
        size_t l = start + 1, r = end;
        int pivot = nums[start];
        while(l < r) {
            while(l < r && nums[l] < pivot)
                l++;
            while(l <= r && nums[r] >= pivot)
                r--;
            if(l < r)
                swap(nums[l], nums[r]);
        }
        
        swap(nums[start], nums[r]);
        return r;
    }

    void qsort(vector<int> &nums, size_t start, size_t end) {
        if(start >= end)
            return;
        size_t q = partition(nums, start, end);
        if(q > 0)
            qsort(nums, start, q - 1);
        qsort(nums, q + 1, end);
    }

    void qsort(vector<int> &nums) {
        qsort(nums, 0, nums.size() - 1);
    }

};

class Solution {
public:
    int maximumGap(vector<int> &nums) {
        if(nums.empty())
            return 0;
        sorting::qsort(nums);
        int ret = 0;
        for(int i=0; i<nums.size()-1; i++)
            ret = max(ret, nums[i+1] - nums[i]);

        return ret;
    }
};

