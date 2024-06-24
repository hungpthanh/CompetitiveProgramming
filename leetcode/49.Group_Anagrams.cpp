class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string> > mp;
        for (const auto& str: strs) {
            string hash = str;
            sort(hash.begin(), hash.end());
            mp[hash].push_back(str);
        }
        vector<vector<string> > results;
        for (const auto& e: mp) results.push_back(e.second);
        return results;
    }
};
