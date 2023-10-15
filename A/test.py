N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))

L = [None] * Q
R = [None] * Q

for i in range(Q):
    L[i], R[i] = list(map(int, input().split()))

S = [None] * (N+1)
S[0] = 0

for j in range(N):
    S[j+1] = S[j] + A[j]
for j in range(Q):
    print(S[R[j]] - S[L[j] - 1])