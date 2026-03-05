import random

class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.val_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.nums.append(val)
        self.val_to_index[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        i = self.val_to_index[val]
        last = self.nums[-1]

        
        self.nums[i] = last
        self.val_to_index[last] = i

        
        self.nums.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)