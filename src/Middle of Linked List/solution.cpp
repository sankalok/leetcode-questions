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
    int lengthList(ListNode* head) {
        int l = 0;
        while(head->next != NULL) {
            l += 1;
            head = head->next;
        } 
        return l+1;
    }
    ListNode* middleNode(ListNode* head) {
        int L = lengthList(head);
        for(int i = 1; i <= L/2; i++) {
            head = head->next;
        }
        return head;
    }
};
