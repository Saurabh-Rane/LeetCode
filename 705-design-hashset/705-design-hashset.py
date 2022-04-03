class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.bucket = [[] for i in range(self.size)]
    
    def hashing(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        index = self.hashing(key)
        if key not in self.bucket[index]:
            self.bucket[index].append(key)

    def remove(self, key: int) -> None:
        index = self.hashing(key)
        if key in self.bucket[index]:
            self.bucket[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self.hashing(key)
        if key in self.bucket[index]:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)