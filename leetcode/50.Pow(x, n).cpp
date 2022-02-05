class Solution {
public:
    double myPow(double x, long long n) {
        if (n < 0) return (double)(1) / myPow(x, -n);
        if (n == 0) return 1;
        if (n == 1) return x;
        if (n % 2 == 0) {
            double half = myPow(x, n / 2);
            return half * half;
        }
        return myPow(x, n - 1) * x;
    }
};
