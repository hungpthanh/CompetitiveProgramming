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
    int result;
    
    void f(TreeNode* root, int sum) {
        if ((root->left == nullptr) && (root->right == nullptr)){
            result += sum;
            return;
        }
        if (root->left != nullptr) f(root->left, sum * 10 + root->left->val);
        if (root->right != nullptr) f(root->right, sum * 10 + root->right->val);
    }
    
    int sumNumbers(TreeNode* root) {
        if (root == nullptr) return 0;
        result = 0;
        f(root, root->val);
        return result;
    }
};
