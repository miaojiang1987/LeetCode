namespace sorting {
    size_t partition(vector<int> &nums, size_t start, size_t end) {
        if(start >= end)
            return end;
        if(start == end - 1) {
            if(nums[start] < nums[end])
                swap(nums[start], nums[end]);
            return end;
        }
        size_t mid = start + (end-start) / 2;
        swap(nums[start], nums[mid]);
        size_t l = start + 1, r = end;
        int pivot = nums[start];
        while(l < r) {
            while(l < r && nums[l] > pivot)
                l++;
            while(l <= r && nums[r] <= pivot)
                r--;
            if(l < r)
                swap(nums[l], nums[r]);
        }
        
        swap(nums[start], nums[r]);
        return r;
    }
};

class Solution {
public:
    int findKthLargest(vector<int> &nums, int k) {
        size_t start = 0, end = nums.size() - 1;
        k--;
        while(start <= end) {
            //cout << "start = " << start << " end = " << end << " k = " << k << endl;
            size_t q = sorting::partition(nums, start, end);
            //cout << "q = " << q << endl;
            if(q == k)
                return nums[q];
            if(q < k) {
                //k -= q-start+1;
                start = q+1;
            }
            else {
                end = q-1;   
            }
        }
        return -1;
    }
};



