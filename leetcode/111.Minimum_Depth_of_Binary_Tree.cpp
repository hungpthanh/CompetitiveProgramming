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
    int minDepth(TreeNode* root) {
        
        if (root == nullptr) return 0;
        int ans = 1;
        int L = minDepth(root->left);
        int R = minDepth(root->right);
        if (L == 0) L = int(1e6);
        if (R == 0) R = int(1e6);
        ans = min(L, R) + 1;
        if (ans > int(1e6)) ans = 1;
        return ans;
    }
};
