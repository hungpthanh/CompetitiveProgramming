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
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == nullptr) return nullptr;
        if (head->next == nullptr) return head;
        int ok = 0;
        while ((head->next != nullptr) && (head->val == head->next->val)) {
            ok = 1;
            head = head->next;    
        }
        
        if (ok == 1) {
            return deleteDuplicates(head->next);
        }
        else {
            head->next = deleteDuplicates(head->next);
            return head;
        }
    }
};
