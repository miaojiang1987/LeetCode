class Node:
    def __init__(self, val, _next=None):
        self.val = val
        self.next = _next

class MyLinkedList(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=None
        self.tail=None
        self.size=0
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index<0 or index>=self.size:
            return -1
        
        current=Node(0,self.head)
        for i in range(index+1):
            current=current.next
        return current.val
            

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        toAdd=Node(val,self.head)
        self.head=toAdd
        if self.size==0:
            self.tail=toAdd
        
        self.size+=1
        
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        toAdd=Node(val)
        if self.size==0:
            self.head=self.tail=toAdd
        else:
            self.tail.next=toAdd
            self.tail=toAdd     
        self.size+=1
        
    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index<0 or index>self.size: return
        if index==0: return self.addAtHead(val)
        if index==self.size: return self.addAtTail(val)
        
        current=Node(0,self.head)
        for i in range(index):
            current=current.next
        toAdd=Node(val,current.next)
        current.next=toAdd
        self.size+=1
        
        
        
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size: return
        current=Node(0,self.head)
        for i in range(index):
            current=current.next
        current.next=current.next.next
        if index==0:
            self.head=current.next
        
        if index==self.size-1:
            self.tail=current
        
        self.size-=1