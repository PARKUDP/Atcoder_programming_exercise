#参考にしながらしましたので、もう1回する必要がある。
N, Q = map(int, input().split())
A = list(map(int, input().split()))

L = [None] * Q
R = [None] * Q

for j in range(Q):
    L[j], R[j] = map(int, input().split())
    
S = [None] * (N+1)
S[0] = 0

for i in range(N):
    S[i+1] = S[i] + A[i]
for j in range(Q):
    print(S[R[j]] - S[L[j]-1])
"""時間超過してしまった。全探索であるから。1回目
for i in range(Q):
    L_list.append(list(map(int, input().split())))
    
for l in L_list:
    start_point = l[0]
    stop_point = l[1]
    for j in range(start_point, stop_point+1):
        answer += A_list[j-1]
    print(answer)
    answer = 0
"""
