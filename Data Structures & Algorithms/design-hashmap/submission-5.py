class MyHashMap:

    def __init__(self):
        self.hash_map=[]

    def put(self, key: int, value: int) -> None:
        if len(self.hash_map)==0:
            self.hash_map.append([key,value])
            return None
        for index in range(0,len(self.hash_map)):
            if self.hash_map[index][0]==key:
                self.hash_map[index][0:2]=key,value
                return None
        self.hash_map.append([key,value])

    def get(self, key: int) -> int:
        for keyer in self.hash_map:
            if keyer[0]==key:
                return keyer[1]
        return -1

    def remove(self, key: int) -> None:
        if len(self.hash_map)==0:
            return None
        for index in range(len(self.hash_map)):
            if self.hash_map[index][0]==key:
                self.hash_map.remove(self.hash_map[index])
                return None