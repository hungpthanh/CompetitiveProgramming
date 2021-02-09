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
    vector<int> results;
    int kthSmallest(TreeNode* root, int k) {
        int kth = -1;
        if (root->left != nullptr) {
            kth = kthSmallest(root->left, k);
            if (kth != -1) return kth;
        }
        results.push_back(root->val);
        if (results.size() >= k) return results[k - 1];
        if (root->right != nullptr) {
            kth = kthSmallest(root->right, k);
            if (kth != -1) return kth;
        }
        if (results.size() >= k) return results[k - 1]; 
        return -1;
    }
};
