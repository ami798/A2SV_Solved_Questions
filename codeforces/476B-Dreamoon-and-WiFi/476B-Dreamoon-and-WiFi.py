import math

s1 = input().strip()
s2 = input().strip()

target = s1.count('+') - s1.count('-')
current = s2.count('+') - s2.count('-')
q = s2.count('?')

diff = target - current


if (diff + q) % 2 != 0:
    print(0.0)
else:
    x = (diff + q) // 2
    if x < 0 or x > q:
        print(0.0)
    else:
        prob = math.comb(q, x) / (2 ** q)
        print(prob)