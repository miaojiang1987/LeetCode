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
    bool isPalindrome(ListNode *head) {
        if(head == nullptr)
            return true;
        vector<ListNode *> nodes;
        
        while(head != nullptr) {
            nodes.push_back(head);
            head = head->next;
        }
        
        size_t len = nodes.size();
        for(size_t i=0; i<len/2; i++) {
            if(nodes[i]->val != nodes[len-1-i]->val)
                return false;
        }
        return true;
    }

};