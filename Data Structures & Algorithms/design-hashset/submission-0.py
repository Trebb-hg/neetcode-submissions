class MyHashSet:

    def __init__(self):
        self.hash=[]
        return None

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hash.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hash.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.hash
