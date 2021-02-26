class Solution {
public:
    int candy(vector<int>& ratings) {
        vector<pair<int, int> > c;
        vector<int> candy;
        for (int i = 0; i < ratings.size(); ++i) {
            c.push_back(make_pair(ratings[i], i));
            candy.push_back(0);
        }
        sort(c.begin(), c.end());
        for (int i = 0; i < c.size(); ++i) {
            int rate = c[i].first;
            int pos = c[i].second;
            if (candy[pos] == 0) candy[pos] = 1;
            if ((pos - 1 >= 0) && (ratings[pos - 1] > ratings[pos])) candy[pos - 1] = max(candy[pos -1] , candy[pos] + 1);
            if ((pos + 1 < ratings.size()) && (ratings[pos + 1] > ratings[pos])) candy[pos + 1] = max(candy[pos + 1], candy[pos] + 1);
        }
        int res = 0;
        for (int i = 0; i < candy.size(); ++i) res += candy[i];
        return res;
    }
};
