class SnapshotArray(object):

    def __init__(self, length):

        self.id = -1
        self.items = []
        self.arr = {}

    def set(self, index, val):

        self.arr[index] = val
        
    def snap(self):

        self.items.append(self.arr)
        self.arr = self.arr.copy()
        self.id += 1
        return self.id 
        
    def get(self, index, snap_id):

        try:
            d = self.items[snap_id]
            return d[index]
        except KeyError:
            return 0