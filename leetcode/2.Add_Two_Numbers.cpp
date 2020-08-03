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
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int add = 0;
        ListNode *res, *start;
        res = new ListNode(0, nullptr);
        start = res;
        while (l1 != nullptr && l2 != nullptr) {
            res-> next = new ListNode();
            res = res-> next;
            res->val= (l1->val + l2->val + add) % 10;
            add = (l1->val + l2->val + add) / 10;
            l1 = l1->next;
            l2 = l2->next;
        }
        if (l1 == nullptr) {
            while (l2 != nullptr) {
                res-> next = new ListNode();
                res = res-> next;
                res->val =(l2->val + add) % 10;
                add = (l2->val + add) / 10;
                l2 = l2->next;
            }
        }
        else {
            while (l1 != nullptr) {
                res-> next = new ListNode();
                res = res-> next;
                res->val =(l1->val + add) % 10;
                add = (l1->val + add) / 10;
                l1 = l1->next;
            }
        }
        
        if (add > 0) {
            res-> next = new ListNode();
            res = res-> next;
            res->val = add;
        }
        
        return start->next;
    }
};
