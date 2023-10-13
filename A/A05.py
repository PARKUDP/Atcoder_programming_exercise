N, K = list(map(int, input().split()))

#比較する対象の変数、カウントする変数
count = int()
pair_number = int()
"""
赤、青、白カードのリスト作成 (結構全探索だと思う。これだと、時間は結構かかると思う。(他のアルゴリズムを工夫する必要がある。よって、通らない。)
その前に、問題の理解が間違っていることに気づいた。

red_card : list[int]= [r for r in range(1, N+1)]
blue_card : list[int] = [b for b in range(1, N+1)]
shiro_card : list[int] = [w for w in range(1, N+1)]
for r in red_card:
    for b in blue_card:
        for s in shiro_card:
            pair_number = r + b + s
            if(pair_number == K):
                count += 1
                

s = 0
for i in range(1, N+1):
    n2max = min(N, K-i-1) 
    n2min = max(1, K-i-N) 
    s += max(n2max-n2min +1, 0)
"""
for x in range(1, N+1):
    for y in range(1, N+1):
        z = K - x - y
        if (z >= 1) and (z <= N):
            count += 1

print(s)
print(count)
