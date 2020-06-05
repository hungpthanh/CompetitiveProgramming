/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
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
    bool isSubPath2(ListNode* head, TreeNode* root) {
        bool res1, res2, res3, res4;
        if (root == nullptr) return false;
        if (head->next == nullptr) return true;
        
       
        
        if (head->val == root->val) {
            res1 = isSubPath2(head->next, root->left);
            res2 = isSubPath2(head->next, root->right);
        }
        else return false;
        return (res1 | res2);
    }
    
    bool isSubPath(ListNode* head, TreeNode* root) {
        bool res1, res2, res3, res4;
        if (root == nullptr) return false;
        if (head->next == nullptr) return true;
        
        
        if (head->val == root->val) {
            res1 = isSubPath2(head->next, root->left);
            res2 = isSubPath2(head->next, root->right);
        }
        res3 = isSubPath(head, root->left);
        res4 = isSubPath(head, root->right);
        return (res1 | res2 | res3 | res4);
    }
};
