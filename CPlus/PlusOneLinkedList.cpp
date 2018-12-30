/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *plusOne(ListNode *head) {
        int carry = plusOneRec(head);
        if(carry > 0) {
            ListNode *ret = new ListNode(1);
            ret->next = head;
            return ret;
        }
        return head;
    }
    
    int plusOneRec(ListNode *head) {
        if(head->next == nullptr) {
            int carry =  (head->val + 1) / 10;
            head->val++;
            head->val %= 10;
            return carry;
        }
        int next = plusOneRec(head->next);
        int carry = (next + head->val) / 10;
        head->val += next;
        head->val %= 10;
        return carry;
    }
};


