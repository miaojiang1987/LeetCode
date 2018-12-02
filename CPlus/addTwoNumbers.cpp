class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy=new ListNode(-1);
        ListNode* cur= dummy;                
        int flag=0;
        while (l1 || l2){
            int val1=l1?l1->val:0;
            int val2=l2?l2->val:0;
            int sum=val1+val2+flag;
            cur->next=new ListNode(sum%10);
            flag=sum/10;
            cur=cur->next;
            if (l1) l1=l1->next;
            if (l2) l2=l2->next;
            
        }
        if (flag) cur->next = new ListNode(1);
        return dummy->next;
    }
};