import sys
read = sys.stdin.readline

x, y = read().strip(), read().strip()
h, w = len(x), len(y)
lcs = [[0] * (w + 1) for _ in range(h + 1)]

for i in range(1, h+1):
    for j in range(1, w+1):
        if x[i - 1] == y[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])
print(lcs[-1][-1])