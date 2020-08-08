class Solution {
public:
    double mincostToHireWorkers(vector<int>& quality, vector<int>& wage, int K) {
        multiset<double, greater<double> > Q;
        vector<pair<double, double> > qw;
        vector<int> sortarr;
        for (int i = 0; i < quality.size(); ++i) qw.push_back(make_pair(double(wage[i]) / (double)(quality[i]), double(quality[i])));
        sort(qw.begin(), qw.end());
        double sum = 0;
        for (int i = 0; i < K; ++i) {
            sum += qw[i].second;
            Q.insert(qw[i].second);
        }
        double res;
        res = qw[K - 1].first * sum;
        for (int i = K; i < qw.size(); ++i) {
            sum -= *Q.begin();
            sum += qw[i].second;
            res = min(res, (double)(qw[i].first) * sum);
            if (qw[i].second >= *Q.begin()) {
                sum +=*Q.begin();
                sum -= qw[i].second;
            }
            Q.insert(qw[i].second);
            Q.erase(Q.begin());
         }
        return res;
    }
};
