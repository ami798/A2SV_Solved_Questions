class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = []
        for target in range(n,1,-1):
            i = arr.index(target)
            if i == target - 1:
                continue
            if i != 0:
                temp = arr[0:i+1] 
                temp.reverse()
                for j in range(len(temp)):
                    arr[j] = temp[j]
                res.append(len(temp))

            temp = arr[0:target]
            temp.reverse()
            for k in range(len(temp)):
                arr[k] = temp[k]
            res.append(target)
        return res
                

            





