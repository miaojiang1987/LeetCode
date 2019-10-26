class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap={}
        self.list=[]
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.hashmap:
            self.list.append(val)
            self.hashmap[val]=len(self.list)-1
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.hashmap:
            return False
        
        index=self.hashmap[val]
        node=self.list.pop()
        
        if index<len(self.list):
            self.list[index]=node
            self.hashmap[node]=index 
        del self.hashmap[val]
        return True
        
    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.list)