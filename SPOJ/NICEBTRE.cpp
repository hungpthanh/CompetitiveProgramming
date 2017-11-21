#include <bits/stdc++.h>
using namespace std;

string s;

void solve() {
    stack <pair<int, int> > st;
    int n = s.size();
    if (n == 1) {
        cout << '0' << endl;
        return ;
    }
    else {
        int res = 0;
        st.push(make_pair(0, 0));
        for (int i = 0; i < n; i++) {
            pair <int, int> cur = st.top();
            res = max(res, cur.second);
            if (s[i] == 'n') {
                st.push(make_pair(0, cur.second + 1));
            }
            else {
                while ((st.size() > 0) && (cur.first == 1)) {
                    st.pop();
                    cur = st.top();
                }
                st.pop();
                st.push(make_pair(1, cur.second));
            }
        }
        cout << res << endl;
    }
}

int main() {
    int test;
    cin >> test;
    for (int t = 1; t <= test; t++) {
        cin >> s;
        solve();
    }
}
