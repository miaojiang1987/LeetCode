class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        
        
        return self.helper(head,None)
         
    
    def helper(self,start,end):
        if start==end:
            return
        
        slow=fast=start
        
        while fast!=end and fast.next!=end:
            slow=slow.next
            fast=fast.next.next
        
        root=TreeNode(slow.val)
        
        root.left=self.helper(start,slow)
        root.right=self.helper(slow.next,end)
        
        return root
        