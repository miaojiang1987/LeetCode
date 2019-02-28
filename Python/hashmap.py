class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.storage=[[] for _ in range(1000)]

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        isFound=False
        hashkey=hash(key)%(len(self.storage))
        for i,(k,v) in enumerate(self.storage[hashkey]):
            if key==k:
                self.storage[hashkey][i]=(key,value)
                isFound=True
                break
        if not isFound:
            self.storage[hashkey].append((key,value))
        
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hashkey=hash(key) % (len(self.storage))
        for k,v in self.storage[hashkey]:
            if k==key:
                return v
        
        return -1
        
        
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        hashkey=hash(key)%(len(self.storage))
        for i,(k,v) in enumerate(self.storage[hashkey]):
            if k==key:
                del self.storage[hashkey][i]