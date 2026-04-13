# n=int(input(list()))
# left,right=0,n-1
# for _ in range(n):
    
#         if left<right:
#                 print(True)
#         else:
#                 print(False)
            

n,r=map(int(list(input)))
for i in range(n):
    for j in range(r):
        print(n.join(r).sort())


