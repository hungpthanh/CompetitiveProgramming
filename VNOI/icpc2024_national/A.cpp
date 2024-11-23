#include<bits/stdc++.h>
using namespace std;

const int maxn = 3 * 1e5;
int n_test, n;
int a[maxn + 5];
map<int, int> counter;

void enter() {
    cin >> n;
    for (int i = 1; i <= n; ++i) cin >> a[i];
}

void solve() {
    counter.clear();
    for (int i = 1; i <= n; ++i) ++counter[a[i]];
    int smaller = 0;
    long long res = 0;
    for (const auto& pair: counter) {
        int c;
        c = pair.second;
        if (c > 2) res += ((long long) 1 * c * (c - 1) * (c - 2)) / 6;
        if (c > 1) res += ((long long) 1 * (c * (c - 1)) / 2) * smaller;
        smaller += c;
    }
    cout << res << endl;
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("test.in", "r", stdin);
    // freopen("test.out", "w", stdout);
    cin >> n_test;
    for (int t = 1; t <= n_test; ++t) {
        enter();
        solve();
    }
    return 0;
}