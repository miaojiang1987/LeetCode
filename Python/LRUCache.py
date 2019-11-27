class DoubLinkedList():
    def __init__(self):
        self.val=0
        self.prev=None
        self.next=None
        self.key=None
        

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head=DoubLinkedList()
        self.tail=DoubLinkedList()
        self.hashmap={}
        self.head.next=self.tail
        self.tail.prev=self.head
        self.capacity=capacity
    
    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
        

    def add2head(self,node):
        node.next=self.head.next
        node.prev=self.head
        node.next.prev=node
        self.head.next=node
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hashmap:
            node=self.hashmap[key]
            self.remove(node)
            self.add2head(node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.hashmap:
            new_node=DoubLinkedList()
            new_node.key=key
            new_node.val=value
            if len(self.hashmap) >= self.capacity:
                last = self.tail.prev
                self.remove(last)
                del self.hashmap[last.key]
            self.add2head(new_node)
            self.hashmap[key]=new_node
        else:
            node = self.hashmap[key]
            node.val = value
            self.remove(node)
            self.add2head(node)
