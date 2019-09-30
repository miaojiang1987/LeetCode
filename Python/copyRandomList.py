"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        hashmap={}
        dummy=new=Node(-1,None,None)
        cur=head        
        
        while cur:            
            new_node=Node(cur.val,None,None)
            hashmap[cur]=new_node
            new.next=new_node
            new=new.next
            cur=cur.next
        
        cur=head
        
        while cur:
            if cur.random:
                hashmap[cur].random=hashmap[cur.random]
            cur=cur.next
        
        
        return dummy.next