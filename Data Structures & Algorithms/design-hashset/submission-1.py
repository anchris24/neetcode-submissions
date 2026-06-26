class MyHashSet:

    def __init__(self):
        self.myhash = []

    def add(self, key: int) -> None:
        if key not in self.myhash:
            self.myhash.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.myhash:
            self.myhash.remove(key)
        

    def contains(self, key: int) -> bool:
        return (key in self.myhash)
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)