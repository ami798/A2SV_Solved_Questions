class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = []
        self.value = value
        self.k = k
        #self.ans = []

    def consec(self, num: int) -> bool:
        if num != self.value:
            self.stream.clear()
        else:
            self.stream.append(num)
            #self.ans.append(len(self.stream) >= self.k)
        return len(self.stream) >= self.k
        #return self.ans
        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)