
n = int(input())
splits = 0
arr=[]
tower=[]
for _ in range(n):
    data = list(map(int, input().split()))
    k = data[0]
    blocks = data[1:]
    
    arr.extend(blocks)
    tower.append(blocks)
arr.sort()

pos= dict()


for i in range(len(arr)):
    pos[arr[i]] = i
for i in range(len(tower)):
    for j in range(len(tower[i])-1):
        x=pos[tower[i][j]]
        if x+1 < len(arr) and tower[i][j+1] !=arr[x+1]:
            
            splits+=1
        if x+1==len(arr):
            splits+=1
        
combine=(n+splits)-1
print(splits,combine)

        




        
        


