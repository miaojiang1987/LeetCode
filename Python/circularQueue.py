class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.queue = []
        self.size = k
        self.count = 0

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.count < self.size:
            self.queue.append(value)
            self.count += 1
            return True
        else:
            return False

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.count > 0:
            self.queue.pop(0)
            self.count -= 1
            return True
        else:
            return False

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.count > 0:
            return self.queue[0]
        else:
            return -1

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.count > 0:
            return self.queue[self.count - 1]
        else:
            return -1
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.count==0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.count == self.size