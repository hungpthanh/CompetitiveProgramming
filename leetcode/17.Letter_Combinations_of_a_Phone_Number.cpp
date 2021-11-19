class Solution {
public:
    vector<string> results;
    string keyboard[10] = {"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    string answer = "";    
    vector<string> letterCombinations(string digits) {
        if (digits.size() == 0) return results;
        backtrack(0, digits);
        return results;
    }
    
    void backtrack(int i, string digits) {
        if (i == digits.size()) {
            results.push_back(answer);
            return;
        }
        int nb = digits[i] - '0';
        for (int j = 0; j < keyboard[nb].size(); ++j) {
            answer += keyboard[nb][j];
            backtrack(i + 1, digits);
            answer.pop_back();
        }
    }
};
