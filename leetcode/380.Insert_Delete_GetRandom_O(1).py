class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.val_to_index = {}
        self.len = 0

    def insert(self, val: int) -> bool:
        if val not in self.val_to_index:
            self.len += 1
            self.val_to_index[val] = self.len - 1
            if len(self.arr) >= self.len:
                self.arr[self.len - 1] = val
            else:
                self.arr.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.val_to_index:
            last_value = self.arr[self.len - 1]
            pos = self.val_to_index[val]
            self.arr[self.val_to_index[val]], self.arr[self.len - 1] = self.arr[self.len - 1], self.arr[self.val_to_index[val]]
            self.len -= 1
            self.val_to_index[last_value] = pos
            del self.val_to_index[val]
            return True
        return False

    def getRandom(self) -> int:
        # print(self.arr)
        index = random.randint(0, self.len - 1)
        return self.arr[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
