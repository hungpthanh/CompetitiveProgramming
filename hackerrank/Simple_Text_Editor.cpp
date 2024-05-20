#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stack>
using namespace std;

int Q, q;
stack<string> st;
string S, W;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    cin >> Q;
    S = "";
    int k;
    for (int t = 0; t < Q; ++t) {
        cin >> q;
        if (q == 1) {
            cin >> W;
            st.push(S);
            S = S + W;
        }
        else if (q == 2) {
            cin >> k;
            st.push(S);
            S.erase(S.size() - k, k);
        }
        else if (q == 3) {
            cin >> k;
            cout << S[k - 1] << endl;
        }
        else {
            if (st.size() > 0) {
                S = st.top();
                st.pop();    
            }
            
        }
    }
    return 0;
}
