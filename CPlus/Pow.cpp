class Solution {
public:
    double myPow(double x, int n) {
        double result=1.0;
        for (int i=n;i!=0;i=i/2){
            if (i%2!=0) result*=x;
            x*=x;
        }
        return n < 0 ? 1 / result : result;
    }
};