'''
H, W = list(map(int, input().split()))
X_list = list()
Q_list = list()

total_X = int()
total_Q = int()
for i in range(H):
    X_list.append(list(map(int, input().split())))
Q = int(input())
for j in range(Q):
    Q_list.append(list(map(int, input().split())))

for i in range(H):
        total_X += sum(X_list[i])

for j in range(Q):
    total_Q += sum(Q_list[j])

print(total_Q)
print(total_X)

問題を理解し間違った。
''' 
H, W = map(int, input().split())
V = [list(map(int,input().split())) for _ in range(H)]
Q = int(input())

Xsum = [[0]*(W+1) for _ in range(H)]
for y in range(H):
    s = 0
    for x in range(W):
        s = s + V[y][x]
        Xsum[y][x+1] = s

for _ in range(Q):
    A, B, C, D =map(int, input().split())
    Ans = 0
    for y in range(A,C+1):
        Ans += (Xsum[y-1][D] - Xsum[y-1][B-1])
    print(Ans)
