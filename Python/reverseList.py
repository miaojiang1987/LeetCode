# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev,cur,nxt=None,head,None
        
        #1->2->3
        #1<-2<-3
        
        while cur!=None:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        
        
        return prev