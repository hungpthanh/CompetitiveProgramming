class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        vector<vector<int> > results = board;
        int m = board.size();
        int n = board[0].size();
        int cx[8] = {-1, 0, 1, -1, 1, -1, 0, 1};
        int cy[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j) {
                int n_live = 0;
                for (int k = 0; k < 8; ++k) {
                    int nx = i + cx[k];
                    int ny = j + cy[k];
                    if ((nx >= 0) && (nx < m) && (ny >= 0) && (ny < n)) n_live += board[nx][ny];
                }
                if (board[i][j] == 1) {
                    if ((n_live < 2) or (n_live > 3)) results[i][j] = 0;
                    else results[i][j] = 1;
                }
                else {
                    if (n_live == 3) results[i][j] = 1;
                }
            }
        board = results;   
    }
};
