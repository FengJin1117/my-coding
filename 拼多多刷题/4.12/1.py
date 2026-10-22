# 差分数组 + 前缀和
'''
设水泥路c段，
成本：2m - c。c越大，时间越短
m 已知，其实就是统计c。这条赛道有多少水泥路。
每次操作，对应区间都+1。用差分操作区间
'''

# =========================
# 调试
# =========================
from io import StringIO
import sys

sys.stdin = StringIO("""3 2
1 2
2 3
""")

import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())

    # 差分数组
    d = [0]* (n+2)
    # 读入区间操作
    for _ in range(m):
        l, r = map(int, input().split())
        d[l] += 1
        d[r+1] -= 1

    # 前缀和还原
    max_c = 0
    best_id = 1
    cur = 0
    for i in range(1, n+1):
        cur += d[i]
        if cur > max_c:
            max_c = cur
            best_id = i

    print(2*m-max_c, best_id)

solve()