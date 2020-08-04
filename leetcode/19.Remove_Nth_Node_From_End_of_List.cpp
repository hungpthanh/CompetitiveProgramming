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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *start = head;
        int cnt = 0;
        while (head != nullptr) {
            ++cnt;
            head = head->next;
        }
        int idx = cnt - n;
        if (idx == 0) return start->next;
        head = start;
        for (int i = 1; i <= idx - 1; ++i) head = head->next;
        head->next = head->next->next;
        return start;
    }
};
