/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<int> ini;
        queue<pair<int, TreeNode* > > Q;
        vector<vector<int> > final_results, results;
        int h = 0;
        TreeNode* node;
        Q.push(make_pair(0, root));
        
        if (root != NULL) ini.push_back(root->val);

        results.push_back(ini);

        while (!Q.empty()) {
            auto g = Q.front();
            int h = g.first;
            node = g.second;
            if (node != NULL) {
                if (results.size() < h + 2) results.emplace_back();
                if (node->left != NULL) {
                    results[h + 1].push_back(node->left->val);
                    Q.push(make_pair(h + 1, node->left));
                }
                if (node->right != NULL) {
                    results[h + 1].push_back(node->right->val);
                    Q.push(make_pair(h + 1, node->right));
                }
            }
            Q.pop();
        }
        h = 0;
        
        for (auto result: results) {
            if (result.size() == 0) break;
            if (h % 2 == 1) std::reverse(result.begin(), result.end());                
            final_results.push_back(result);
            ++h;
        }
        return final_results;
    }
};
