# ! DPコンテスト

# ! G（最長長さ。有向グラフに関するDP）
# from collections import defaultdict
# import sys
# sys.setrecursionlimit(10**7)
# n, m = map(int, input().split())
# G = defaultdict(list)
# indeg = [0]*n
# for _ in range(m):
#     x, y = map(int, input().split())
#     x, y = x-1, y-1
#     G[x].append(y)
#     indeg[y] += 1

# done = [False] * n
# length = [0] * n

# def dfs(i):
#     if done[i]:
#         return length[i]
    
    
#     for j in G[i]:
#         length[i] = max(length[i], dfs(j) + 1)
#     done[i] = True
#     return length[i]

# for i in range(n):
#     if indeg[i] == 0:
#         dfs(i)

# print(max(length))

# ! 巡回セールスマン問題
n = int(input())
dis = []

for _ in range(n):
    dis.append(list(map(int, input().split())))

inf = 10 ** 20
dp = [[inf]*(n) for _ in range(2**n)] # dp[n][i] すでに訪れた都市の集合nがあって、最後にいる都市がiのときの合計コストの最小値
dp[0][0] = 0 # 最初の出発地は都市0

for N in range(2**n):
    # iからjへの遷移をしらべる
    for i in range(n):
        for j in range(n):
            # すでに訪問済みなら調べない
            if  N & (1 << j) or i == j:
                continue
            dp[N|(1<<j)][j] = min(dp[N|(1<<j)][j], dp[N][i] + dis[i][j])

print(dp[2**n-1][0])