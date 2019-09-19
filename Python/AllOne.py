class ListNode:
    def __init__(self, key, val, isDummy):
        self.key = key
        self.val = val
        self.isDummy = isDummy
        self.prev = None
        self.next = None
    def __str__(self):
        return "Key: " + self.key + " Value: " + str(self.val)
        
class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nodeMap = {}  # Key: key, Value: Node
        self.buckets = [[ListNode("", 0, True)]]  
        self.keyMap = {}  # Key: 
    
    def remove(self, key):
        node = self.nodeMap[key]
        freq = node.val
        if node == self.buckets[freq][0]:
            self.buckets[freq][0] = self.buckets[freq][0].next
            self.buckets[freq][0].prev = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
    
    def add(self, key):
        node = self.nodeMap[key]
        freq = node.val
        if freq == len(self.buckets):
            self.buckets.append([ListNode("dummy", 0, True)])
        conn = self.buckets[freq][0]
        node.next = conn
        conn.prev = node
        self.buckets[freq][0] = node

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.keyMap:
            self.remove(key)
        self.keyMap[key] = self.keyMap.get(key, 0) + 1
        node = self.nodeMap[key] = self.nodeMap.get(key, ListNode(key, 0, False))
        node.val += 1
        self.add(key)
        
    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.keyMap:
            return
        self.remove(key)
        
        if self.keyMap[key] == 1:
            del self.keyMap[key]
            del self.nodeMap[key]
            return
        self.keyMap[key] -= 1
        self.nodeMap[key].val -= 1
        self.add(key)
        
    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        last = len(self.buckets) - 1
        while last >= 0:
            if not self.buckets[last][0].isDummy:
                return self.buckets[last][0].key
            last -= 1
        return ""
        
    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        first = 1
        while first < len(self.buckets):
            if not self.buckets[first][0].isDummy:
                return self.buckets[first][0].key
            first += 1