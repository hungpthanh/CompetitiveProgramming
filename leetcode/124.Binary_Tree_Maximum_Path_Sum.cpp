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
    int max_path = - int(4 * 1e8);
    int maxPath(TreeNode* root) {
        if (root == NULL) return 0;
        TreeNode* left = root->left;
        TreeNode* right = root->right;

        int left_v = maxPath(left);
        int right_v = maxPath(right);
        int current_node = max(root->val + max(left_v, 0), root->val + max(right_v, 0));
        max_path = max(max_path, root->val + max(left_v, 0) + max(right_v, 0));
        return current_node;
    }

    int maxPathSum(TreeNode* root) {
        maxPath(root);
        return max_path;
    }
};
