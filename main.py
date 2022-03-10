def perm(n, left, right):
    global q
    if left >= right:
        q += n
    else:
        i = left
        for j in range(left, right):
            n[j], n[i] = n[i], n[j]
            perm(n, left + 1, right)
            n[j], n[i] = n[i], n[j]


n = 5
q = []
a = []
for i in range(1, n + 1):
    a.append(i)
perm(a, 0, n)
b = []
temp = 1
for w in range(1, n + 1):
    temp *= w
for j in range(0, temp):
    b.append(q[j * n:j * n + n])
s = sorted(b)
for r in s:
    for c in r:
        print(c, end=' ')
    print()
