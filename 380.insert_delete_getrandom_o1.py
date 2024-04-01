from random import choice


class RandomizedSet:
    def __init__(self):
        self.values: list[int] = []
        self.indices: dict[int, int] = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.indices[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        if len(self.values) == 1:
            self.values = []
            self.indices = {}
            return True


        index = self.indices[val]
        del self.indices[val]
        if index == len(self.values)-1:
            self.values.pop(-1)
        else:
            self.indices[self.values[-1]] = index
            self.values[index] = self.values.pop(-1)

        return True

    def getRandom(self) -> int:
        return choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
