from collections import defaultdict

n = int(input())
words = [input() for _ in range(n)]

graph = defaultdict(list)
for i in range(n - 1):
    w1 = words[i]
    w2 = words[i + 1]

    found = False

    for j in range(min(len(w1), len(w2))):

        if w1[j] != w2[j]:
            graph[w1[j]].append(w2[j])
            found = True
            break

    
    if not found and len(w1) > len(w2):
        print("Impossible")
        exit()

state = {}
ans = []
cycle = False

def dfs(u):
    global cycle

    state[u] = 1

    for v in graph[u]:

        if state.get(v, 0) == 0:
            dfs(v)

        elif state[v] == 1:
            cycle = True

    state[u] = 2
    ans.append(u)

for c in "abcdefghijklmnopqrstuvwxyz":

    if state.get(c, 0) == 0:
        dfs(c)

if cycle:
    print("Impossible")
else:
    ans.reverse()
    print("".join(ans))