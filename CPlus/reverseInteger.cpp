class Solution {
public:
    int reverse(int x) {
        bool positive=(x>0);
        if(x == INT_MIN) return 0;
        if(positive!=true) x=-x;
        int result=0;
        while (x>0){
            if(INT_MAX / 10 < result) return 0;
            result = result * 10 + (x % 10);
            x /= 10;
        }
        
        if(positive) return result;
        else return -result;
    }
};