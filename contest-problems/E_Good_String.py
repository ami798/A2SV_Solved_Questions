n = int(input())
s = input().strip()
res = []
out = 0
i = 0
while i < len(s):
    if i + 1<len(s) and s[i]!= s[i+1]:
        res.append(s[i])
        res.append(s[i+1])
        i += 2
    else:
        out += 1
        i += 1
string = "".join(res)
if len(string) % 2 == 1:
    out +=1
    string = string[:-1]
print(out)
if string:
    print(string)




                

