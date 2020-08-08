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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int min_v = INT_MAX;
        int save_idx = -1;
        for (int i = 0; i < lists.size(); ++i) {
            if (lists[i] != nullptr) {
                if (min_v > lists[i]->val) {
                    min_v = min(min_v, lists[i]->val);
                    save_idx = i;
                }
            }
        }
        ListNode *res;
        if (min_v == INT_MAX) return nullptr;
        lists[save_idx] = lists[save_idx]->next;
        res = new ListNode(min_v, mergeKLists(lists));
        return res;
    }
};
