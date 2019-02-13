class Solution {
public:
    double myPow(double x, int n){
      if(x==0.0) return 0;
      if(x == 1) return x;
      if(x == -1.0) {
            return n%2==0 ? 1 : -1;
      }
      if(n == INT_MIN) return 0;  
      if(n<0) return 1/pow(x,-n);
      else return pow(x,n); 
        
    }
    
    double pow(double x, int n){
        if (n==0){
            return 1;
        }
        
        double half=pow(x,n/2);
        if(n%2==0){
            return half*half;
        }
        else{
            return half*half*x;
        }
    }
};