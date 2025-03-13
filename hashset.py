class MyHashSet:
    def __init__(self):
        self.primaryBuckets = 1000
        self.secondaryBuckets = 1000
        self.storage = [None] * self.primaryBuckets

    def getPrimaryHash(self, key):
        return key % self.primaryBuckets

    def getSecondaryHash(self, key):
        return key // self.primaryBuckets

    def add(self, key):
        primaryIndex = self.getPrimaryHash(key)
        if self.storage[primaryIndex] is None:
            if primaryIndex == 0:
                # +1 to handle key = 1_000_000
                self.storage[primaryIndex] = [False] * (self.secondaryBuckets + 1)
            else:
                self.storage[primaryIndex] = [False] * self.secondaryBuckets
        secondaryIndex = self.getSecondaryHash(key)
        self.storage[primaryIndex][secondaryIndex] = True

    def remove(self, key):
        primaryIndex = self.getPrimaryHash(key)
        if self.storage[primaryIndex] is not None:
            secondaryIndex = self.getSecondaryHash(key)
            self.storage[primaryIndex][secondaryIndex] = False

    def contains(self, key):
        primaryIndex = self.getPrimaryHash(key)
        if self.storage[primaryIndex] is not None:
            secondaryIndex = self.getSecondaryHash(key)
            return self.storage[primaryIndex][secondaryIndex]
        return False


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
obj.add(1000000)  # Edge case
print(obj.contains(1))  # True
print(obj.contains(1000000))  # True
obj.remove(1)
print(obj.contains(1))  # False
