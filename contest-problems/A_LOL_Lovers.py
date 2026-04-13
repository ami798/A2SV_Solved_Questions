

n = int(input())
s = input()
count_l = [0] * (n + 1)
count_o = [0] * (n + 1)
for i in range(n):
    if s[i] == 'L':
        count_l[i+1] = count_l[i] + 1
        count_o[i+1] = count_o[i]
    else:
        count_l[i+1] = count_l[i]
        count_o[i+1] = count_o[i] + 1

ans = -1
for k in range(1, n+1):
    if count_l[k] == count_o[n] - count_o[n-k] and count_o[k] == count_l[n] - count_l[n-k]:
        ans = k

print(ans)

















#this code doens't work for all of the test cases please give me woking code please check all the test cases carefuuly and give me working code please 