from collections import defaultdict

class FrequencyTracker:
    def __init__(self):
        self.numCount = defaultdict(int)
        self.freqCount = defaultdict(int)

    def add(self, number: int) -> None:
        oldFreq = self.numCount[number]
        if oldFreq > 0:
            self.freqCount[oldFreq] -= 1

        self.numCount[number] += 1
        newFreq = self.numCount[number]
        self.freqCount[newFreq] += 1

    def deleteOne(self, number: int) -> None:
        if self.numCount[number] == 0:
            return

        oldFreq = self.numCount[number]
        self.freqCount[oldFreq] -= 1

        self.numCount[number] -= 1
        newFreq = self.numCount[number]
        if newFreq > 0:
            self.freqCount[newFreq] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freqCount[frequency] > 0