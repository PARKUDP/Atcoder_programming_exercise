"""

D = int(input())
N = int(input())

L = [None] * (N+1)
Q = [None] * (N+1)

for i in range(1, N+1):
    L[i], Q[i] = list(map(int, input().split()))

S = [0] * (D+1)

for i in range(1, N+1):
    S[L[i]] += 1
    S[Q[i] + 1] -= 1
    
answer = [0] * (D+1)

for j in range(1, D+1):
    answer[j] = answer[j-1] + S[j]
    
for j in range(1, D+1):
    print(answer[j])
１回目(時間超過)
for i in range(N):
    for j in range(L[i], Q[i]+1):
        S[j] += 1

for j in range(1, len(S)):
    print(S[j])
"""
D = int(input())
N = int(input())
L = []
R = []
for _ in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

C = [0]
C.extend([0] * (D + 1))
for i in range(N):
    C[L[i]] += 1
    C[R[i] + 1] -= 1

result_sum = [0]
for i in range(1, D + 1):
    result_sum.append(result_sum[i - 1] + C[i])

result_sum = result_sum[1:]
for sum in result_sum:
    print(sum)