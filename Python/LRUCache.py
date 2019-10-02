class DoubleLinkedNode:
    def __init__(self):
        self.key = None
        self.value = None
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = DoubleLinkedNode()
        self.tail = DoubleLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}
        self.capacity = capacity
        
    def remove(self, node):    # head -> n2 -> n3 ->
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def add2head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.add2head(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            new_node = DoubleLinkedNode()
            new_node.key = key
            new_node.value = value
            if len(self.map) >= self.capacity:
                last = self.tail.prev
                self.remove(last)
                del self.map[last.key]
            self.map[key] = new_node
            self.add2head(new_node)
        
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.remove(node)
            self.add2head(node)