class Solution {
public:
    string getPermutation(int n, int k) {
        int f[n + 5], dd[n + 5];
        f[0] = 1;
        for (int i = 1; i <= n; ++i) {
            f[i] = f[i - 1] * i;
            dd[i] = 0;
        }
        int On = n;
        string res = "";
        while (n > 0) {
            int sum = 0;
            for (int i = 1; i <= On; ++i) if (dd[i] == 0) {
                sum += f[n - 1];
                if (sum >= k) {
                    res += i + '0';
                    dd[i] = 1;
                    k -= (sum - f[n - 1]);
                    --n;
                    break;
                }
            }
        }
        return res;
    }
};
