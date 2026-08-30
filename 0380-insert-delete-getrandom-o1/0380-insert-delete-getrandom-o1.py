import random

class RandomizedSet:

    def __init__(self):
        self.arr = []          # Stores values
        self.pos = {}          # value -> index

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False

        self.pos[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False

        idx = self.pos[val]
        last = self.arr[-1]

        # Move last element into deleted spot
        self.arr[idx] = last
        self.pos[last] = idx

        # Remove last element
        self.arr.pop()
        del self.pos[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)