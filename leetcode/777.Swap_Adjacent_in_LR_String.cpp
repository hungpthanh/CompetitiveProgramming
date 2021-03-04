class Solution {
public:
    bool canTransform(string start, string end) {
        string s_start = "";
        string s_end = "";
        vector<int> pos_s_l;
        vector<int> pos_s_r;
        vector<int> pos_e_l;
        vector<int> pos_e_r;
        
        for (int i = 0; i < start.size(); ++i) {
            if (start[i] != 'X') {
                s_start += start[i];
                if (start[i] == 'L') pos_s_l.push_back(i);
                else pos_s_r.push_back(i);
            }
        }
        for (int i = 0; i < end.size(); ++i) {
            if (end[i] != 'X') {
                s_end += end[i];
                if (end[i] == 'L') pos_e_l.push_back(i);
                else pos_e_r.push_back(i);
            }
            
        }
        if (s_start != s_end) return false;
        for (int i = 0; i < pos_s_l.size(); ++i) {
            if (pos_e_l[i] > pos_s_l[i]) return false;
        }
        
        for (int i = 0; i < pos_s_r.size(); ++i) {
            if (pos_e_r[i] < pos_s_r[i]) return false;
        }
        return true;
    }
};
