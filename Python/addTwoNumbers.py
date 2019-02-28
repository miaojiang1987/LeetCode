class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        if not l2:
            return l1
        if not l1:
            return l2
        
        flag=0
        dummy=ListNode(0)
        current=dummy
        
        while l1 and l2:
            add=(l1.val+l2.val+flag)%10
            flag=(l1.val+l2.val+flag)//10
            current.next=ListNode(add)
            current=current.next
            l1=l1.next
            l2=l2.next
        
        while l1: 
            add= (l1.val+flag)%10
            flag= (l1.val+flag)//10
            current.next=ListNode(add)
            current=current.next
            l1=l1.next
            
        while l2:
            add=(l2.val+flag)%10
            flag=(l2.val+flag)/10
            current.next=ListNode(add)
            current=current.next
            l2=l2.next
            #print(l2.val)
            
        if flag==1:
            current.next=ListNode(flag)
        
        return dummy.next